# Generated by Django 4.0.5 on 2023-01-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agencyName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='agencyNameRequest',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstnameUserRequest',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastnameUserRequest',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userNameAgency',
            field=models.CharField(max_length=255, null=True),
        ),
    ]