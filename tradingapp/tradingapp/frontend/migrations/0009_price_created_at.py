# Generated by Django 3.0.8 on 2020-07-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20200715_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
