# Generated by Django 4.0.5 on 2023-02-01 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appproject', '0002_alter_user_agencyname_alter_user_agencynamerequest_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
