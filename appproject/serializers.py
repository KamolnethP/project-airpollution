from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import User,File,DataUpload,Province,DataSetGroup,Metadata,DataUpload
from django.utils import encoding

class AppProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'agencyName', 'username', 'userNameAgency', 'isAgency']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class FileSerializer(serializers.Serializer):
    def create(self, validated_data):
        files = self.context['files']
        data = self.context['data']
        print("==========")
        print(data)
        dataName = encoding.smart_str(data['dataName'],encoding='utf-8', strings_only=False, errors='strict')
        dataUpload = DataUpload.objects.create( 
            dataName=dataName,
            description=data['description'],
            dataSetgroupId=data['dataSetgroupId'],
            provinceId=data['provinceId'],
            fileName=data['fileName']
         ,**validated_data)
        for file in files:
            File.objects.create( dataUpload=dataUpload ,file=file, fileName=data['fileName'])
        return dataUpload

    class Meta:
        model = File
        fields = '__all__'

