from django.urls import path, include
from .views import (RegisterUserView,
                    LoginUserView,
                    LogoutView,
                    UploadFileView,
                    UploadNewFileView,
                    ReadFileView,
                    MapMetaDataView,
                    SearchDataView,
                    downloadFile)

urlpatterns =[path('registerUserView', RegisterUserView.as_view()),
              path('loginUserView', LoginUserView.as_view()),
              path('logoutView', LogoutView.as_view()),
              path('uploadFileView', UploadFileView.as_view({'post': 'create'}), name='file-upload'),
              path('uploadNewFileView', UploadNewFileView.as_view()),
              path('readFileView', ReadFileView.as_view()),
              path('mapMetaDataView', MapMetaDataView.as_view()),
              path('searchDataView', SearchDataView.as_view()),
              path('downloadFile',downloadFile)
              ]