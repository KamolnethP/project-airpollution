# Generated by Django 4.0.5 on 2023-03-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0008_remove_dataupload_provinceid_dataupload_provincename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='provinceName',
            field=models.CharField(max_length=150),
        ),
    ]