# Generated by Django 4.0.5 on 2023-02-08 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0004_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataupload',
            old_name='descripton',
            new_name='description',
        ),
    ]
