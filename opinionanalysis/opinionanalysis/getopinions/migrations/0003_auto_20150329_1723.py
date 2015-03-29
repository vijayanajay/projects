# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getopinions', '0002_auto_20150329_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
    ]
