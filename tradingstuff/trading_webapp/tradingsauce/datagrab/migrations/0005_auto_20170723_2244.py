# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 17:14
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datagrab', '0004_auto_20170723_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocksymbol',
            name='file',
            field=models.FileField(default='settings.BASE_DIR/csvData/<django.db.models.fields.IntegerField>.csv', storage=django.core.files.storage.FileSystemStorage(location='E:\\finalproject\\trunk\\tradingstuff\\trading_webapp\\tradingsauce\\csvData'), upload_to=''),
        ),
    ]