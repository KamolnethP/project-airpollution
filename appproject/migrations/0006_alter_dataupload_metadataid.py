# Generated by Django 4.0.5 on 2023-02-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0005_rename_descripton_dataupload_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='metaDataId',
            field=models.IntegerField(null=True),
        ),
    ]