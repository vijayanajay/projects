# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 14:55
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datagrab', '0003_auto_20170723_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocksymbol',
            name='file',
            field=models.FileField(default=django.core.files.storage.FileSystemStorage(location='E:\\finalproject\\trunk\\tradingstuff\\trading_webapp\\tradingsauce\\csvData'), storage=django.core.files.storage.FileSystemStorage(location='E:\\finalproject\\trunk\\tradingstuff\\trading_webapp\\tradingsauce\\csvData'), upload_to=''),
        ),
    ]
