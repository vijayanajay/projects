# Generated by Django 3.0.8 on 2020-07-30 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_auto_20200731_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('wap', models.FloatField(blank=True, null=True)),
                ('volume', models.PositiveIntegerField(blank=True, null=True)),
                ('trades', models.PositiveIntegerField(blank=True, null=True)),
                ('turnover', models.FloatField(blank=True, null=True)),
                ('deliverable_quantity', models.IntegerField(blank=True, null=True)),
                ('percent_del_traded_qty', models.FloatField(blank=True, null=True)),
                ('spread_highLow', models.FloatField(blank=True, null=True)),
                ('spread_closeOpen', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Company')),
            ],
            options={
                'unique_together': {('company', 'date')},
            },
        ),
        migrations.CreateModel(
            name='DailyPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('wap', models.FloatField(blank=True, null=True)),
                ('volume', models.PositiveIntegerField(blank=True, null=True)),
                ('trades', models.PositiveIntegerField(blank=True, null=True)),
                ('turnover', models.FloatField(blank=True, null=True)),
                ('deliverable_quantity', models.IntegerField(blank=True, null=True)),
                ('percent_del_traded_qty', models.FloatField(blank=True, null=True)),
                ('spread_highLow', models.FloatField(blank=True, null=True)),
                ('spread_closeOpen', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Company')),
            ],
            options={
                'unique_together': {('company', 'date')},
            },
        ),
    ]