# Generated by Django 2.1.7 on 2019-03-13 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20190313_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='account_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
