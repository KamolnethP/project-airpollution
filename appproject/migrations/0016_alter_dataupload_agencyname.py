# Generated by Django 4.0.5 on 2023-04-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0015_dataupload_agencyname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='agencyName',
            field=models.CharField(max_length=255),
        ),
    ]