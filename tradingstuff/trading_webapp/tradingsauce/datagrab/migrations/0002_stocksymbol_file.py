# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 14:52
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datagrab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksymbol',
            name='file',
            field=models.FileField(default=django.core.files.storage.FileSystemStorage(location='E:\\finalproject\\trunk\\tradingstuff\\trading_webapp\\tradingsauce/media/csvData'), storage=django.core.files.storage.FileSystemStorage(location='E:\\finalproject\\trunk\\tradingstuff\\trading_webapp\\tradingsauce/media/csvData'), upload_to=''),
        ),
    ]
