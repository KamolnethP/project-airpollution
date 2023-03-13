from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status,viewsets
from .models import User,File,DataUpload,Province,DataSetGroup, FieldName
from django.shortcuts import render
import jwt, datetime,csv, codecs
from django.views.decorators.csrf import csrf_exempt
import json
from wsgiref.util import FileWrapper
import pandas as pd
from .serializers import AppProjectSerializer,FileSerializer,ProvinceSerializer,DataSetGroupSerializer


def checktoken(token):

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    except jwt.ExpiredSignatureError:        
        raise AuthenticationFailed('Unauthenticated!')
    return payload


# Create your views here.

class RegisterUserView(APIView):
    def post(self, request):
        serializer = AppProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"statusCode":0,"data":{"result" : serializer.data}} )


class LoginUserView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            data = {
                'statusCode' : 1000,
                'errorMsg' : 'USER_NOT_FOUND'
            }
            return JsonResponse(data, safe=False, status=403)

        if not user.check_password(password):
            data = {
                'statusCode' : 1000,
                'errorMsg' : 'PASSWORD_INVALID'
            }
            return JsonResponse(data, safe=False, status=403)
            

        payload = {
            'userId': user.userId,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1440),
            'iat': datetime.datetime.utcnow(),
            'isAgency': user.isAgency
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'statusCode' : 0,
            'data' : {
                'jwt': token
            }
        }
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'statusCode' : 0,
            'message': 'success'
        }
        return response


class UploadFileView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = DataUpload.objects.all()
    serializer_class = FileSerializer
    def create(self, request):
        files = request.FILES.getlist('files', None)
        province = Province.objects.filter(name_th=request.POST['provinceId']).first()
        dataSet = DataSetGroup.objects.filter(dataSetGroupName=request.POST['dataSetGroupId']).first()
        dataUpload = DataUpload.objects.create(
            dataSetgroupId=dataSet.dataSetGroupId,
            fileName=request.POST['fileName'],
            provinceId=province.provinceid,
            dataName=request.POST['dataName'],
            description=request.POST['description']
            )
        global file_Res 
        for file in files:
            File.objects.create( dataUpload=dataUpload ,file=file, fileName=request.POST['fileName'])
            file_Res = file
        file = pd.read_excel(file_Res)
        return Response(data={"statusCode": 0, "data": file.columns.ravel()}, status=status.HTTP_200_OK)


class ReadFileView(APIView):
    def post(self, request):
        fileName = request.data['fileName']
        file = pd.read_excel("./media/"+fileName)
        return Response(data={"statusCode": 0, "data": file.columns.ravel()}, status=status.HTTP_200_OK)



class UploadNewFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        files = request.FILES.getlist('files', None)
        File.objects.create( file=files, fileName=request.data['fileName'])
        return Response(data={"statusCode":0},status=status.HTTP_201_CREATED)



class MapMetaDataView(APIView):
    def post(self, request):
        for field in request.data['mapFields']:
            FieldName.objects.create(
                dataId=field['dataId'],
                metaDataName=field['metaDataName'],
                fieldName=field['fieldName']
            )
        return Response(data={"statusCode": 0}, status=status.HTTP_200_OK)




class SearchDataView(APIView):
    def post(self, request):
        resultData = DataUpload.objects.none()
        dataSetGroupId = request.data['dataSetGroupId']
        if dataSetGroupId:
            resultData = DataUpload.objects.filter(dataSetgroupId=dataSetGroupId).values()
        keySearch = request.data['keySearch']
        if keySearch and resultData:
            resultData = resultData.filter(description__contains=keySearch).values()
        elif keySearch and not dataSetGroupId:
            resultData = DataUpload.objects.filter(description__contains=keySearch).values()
        metaDataField = request.data['metaDataField']
        if metaDataField and resultData:
            dataIds = FieldName.objects.filter(metaDataName__in=metaDataField).values()
            resultData = resultData.filter().values()
        elif metaDataField and not dataSetGroupId and not keySearch:
            dataIds = FieldName.objects.filter(metaDataName__in=metaDataField).values()
            resultData = DataUpload.objects.filter(pk__in=dataIds).values()
        print(resultData)
        listResultData = list(resultData)
        return Response(data={"statusCode": 0, "data": listResultData}, status=status.HTTP_200_OK)


@csrf_exempt
def downloadFile(request):
    if request.method == "POST":
        mydata = json.loads(request.body)
        filePath = mydata['filePath']
        path = "./media/" + filePath
        print(path)
        FilePointer = open(path, "rb")
        response = HttpResponse(FileWrapper(FilePointer), content_type = 'whatever')
        response['Content-Disposition'] = 'attachment; filename="%s"'%filePath
        return response
        

def dropdownList(request):
    if request.method == "GET":
        province = Province.objects.all()
        dataSetGroup = DataSetGroup.objects.all()
        listprovicne = list(province.values())
        listdataSetGroup = list(dataSetGroup.values())
        return JsonResponse({"statusCode":0,"province":listprovicne, "dataSetGroup":listdataSetGroup},safe=False)
