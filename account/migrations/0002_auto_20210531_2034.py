# Generated by Django 3.1.7 on 2021-05-31 15:04

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloggeraccount',
            name='logo',
            field=models.ImageField(default='/default-img/titlelogo.png', upload_to=account.models.get_uplaod_file_name_blog),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='logo',
            field=models.ImageField(default='/default-img/titlelogo.png', upload_to=account.models.get_uplaod_file_name),
        ),
    ]
