# Generated by Django 2.0.1 on 2018-02-02 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0003_auto_20180130_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userportfolio',
            name='currency_amount',
            field=models.FloatField(),
        ),
    ]
