# Generated by Django 3.0.5 on 2020-05-06 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20200505_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='DATE_CREATED',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 15, 15, 43, 193368)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='DATE_CREATED',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 15, 15, 43, 191369)),
        ),
    ]