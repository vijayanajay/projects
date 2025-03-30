# Generated by Django 2.2.3 on 2020-05-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_company_last_updated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='bom_id',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='price',
            name='rsi',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='sma_periodBig',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='sma_periodSmall',
            field=models.FloatField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together={('company', 'date')},
        ),
    ]
