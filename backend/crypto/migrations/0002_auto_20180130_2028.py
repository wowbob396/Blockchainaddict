# Generated by Django 2.0.1 on 2018-01-31 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usercurrencies',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usercurrencies',
            name='currency_amount',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
