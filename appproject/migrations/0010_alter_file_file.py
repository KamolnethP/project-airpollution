# Generated by Django 4.0.5 on 2023-03-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0009_alter_dataupload_provincename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=models.CharField(max_length=255, null=True)),
        ),
    ]
