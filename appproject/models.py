from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    userId = models.AutoField(primary_key=True)

    agencyName = models.CharField(max_length=255 ,null=True)
    userNameAgency = models.CharField(max_length=255 ,null=True)
    
    firstnameUserRequest = models.CharField(max_length=255 ,null=True)
    lastnameUserRequest = models.CharField(max_length=255 ,null=True)
    agencyNameRequest = models.CharField(max_length=255 ,null=True)

    username = None
    isAgency = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class DataUpload(models.Model):
    dataId = models.AutoField(primary_key=True)
    dataName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dataSetgroupId = models.IntegerField()
    provinceName = models.CharField(max_length=150)
    fileName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.__all__


class File(models.Model):
    dataUpload = models.ForeignKey(DataUpload, related_name="file", on_delete=models.CASCADE) 
    fileName = models.CharField(null=True, max_length=255)
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.__all__


class FieldName(models.Model):
    fieldName = models.CharField(max_length=255)
    metaDataName = models.CharField(max_length=255)
    dataId = models.IntegerField()
    def __str__(self):
        return self.__all__


class Metadata(models.Model):
    metadataId = models.AutoField(primary_key=True)
    metadataName = models.CharField(max_length=100) 

    def __str__(self):
        return self.__all__


class DataSetGroup(models.Model):
    dataSetGroupId = models.IntegerField(primary_key=True)
    dataSetGroupName = models.CharField(max_length=100) 

    def __str__(self):
        return self.__all__


class Province(models.Model):
    provinceid = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=2)
    name_th = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    geography_id = models.IntegerField()

    def __str__(self):
        return self.__all__


class Download(models.Model):
    fileName = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    countView = models.IntegerField()

    def __str__(self):
        return self.__all__