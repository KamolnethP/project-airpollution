from django.urls import path, include
from .views import (RegisterUserView,
                    LoginUserView,
                    LogoutView,
                    UploadFileView,
                    MapMetaDataView,
                    SearchDataView,
                    downloadFile,
                    dropdownList,
                    ListAgencyView,
                    ListDataAgencyView)

urlpatterns =[path('registerUserView', RegisterUserView.as_view()),
              path('loginUserView', LoginUserView.as_view()),
              path('logoutView', LogoutView.as_view()),
              path('uploadFileView', UploadFileView.as_view({'post': 'create'}), name='file-upload'),
              path('mapMetaDataView', MapMetaDataView.as_view()),
              path('searchDataView', SearchDataView.as_view()),
              path('downloadFile',downloadFile),
              path('dropdownList',dropdownList),
              path('listAgencyView', ListAgencyView.as_view()),
              path('listDataAgencyView', ListDataAgencyView.as_view())
              ]