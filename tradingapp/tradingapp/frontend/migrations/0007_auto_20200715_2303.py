# Generated by Django 3.0.8 on 2020-07-15 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_company_yahoo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='deliverable_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='percent_del_traded_qty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='spread_closeOpen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='spread_highLow',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='trades',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='turnover',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='volume',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='wap',
            field=models.FloatField(blank=True, null=True),
        ),
    ]