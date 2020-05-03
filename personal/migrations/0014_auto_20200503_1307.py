# Generated by Django 3.0.5 on 2020-05-03 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0013_auto_20200502_2214'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='wallet',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
