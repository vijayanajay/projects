# Generated by Django 3.0.8 on 2020-07-23 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_price_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyStockStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('mean', models.FloatField(blank=True, null=True)),
                ('std_dev', models.FloatField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Company')),
            ],
            options={
                'unique_together': {('company', 'date')},
            },
        ),
    ]
