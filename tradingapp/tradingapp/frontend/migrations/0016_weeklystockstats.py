# Generated by Django 3.0.8 on 2020-08-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_auto_20200806_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyStockStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day_high', models.FloatField(blank=True, null=True)),
                ('day_low', models.FloatField(blank=True, null=True)),
                ('mean', models.FloatField(blank=True, null=True)),
                ('std_dev', models.FloatField(blank=True, null=True)),
                ('rsi', models.FloatField(blank=True, null=True)),
                ('macd', models.FloatField(blank=True, null=True)),
                ('stochastic', models.FloatField(blank=True, null=True)),
                ('roc', models.FloatField(blank=True, null=True)),
                ('willr', models.FloatField(blank=True, null=True)),
                ('mfi', models.FloatField(blank=True, null=True)),
                ('atr', models.FloatField(blank=True, null=True)),
                ('adx', models.FloatField(blank=True, null=True)),
                ('bol_high', models.FloatField(blank=True, null=True)),
                ('bol_low', models.FloatField(blank=True, null=True)),
                ('sma_5', models.FloatField(blank=True, null=True)),
                ('sma_10', models.FloatField(blank=True, null=True)),
                ('sma_20', models.FloatField(blank=True, null=True)),
                ('sma_50', models.FloatField(blank=True, null=True)),
                ('sma_100', models.FloatField(blank=True, null=True)),
                ('sma_200', models.FloatField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Company')),
            ],
            options={
                'unique_together': {('company', 'date')},
            },
        ),
    ]
