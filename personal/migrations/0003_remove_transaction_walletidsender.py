# Generated by Django 3.0.5 on 2020-04-30 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20200430_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='walletIdSender',
        ),
    ]
