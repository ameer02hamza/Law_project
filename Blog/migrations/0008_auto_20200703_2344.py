# Generated by Django 3.0.6 on 2020-07-03 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20200703_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 23, 44, 29, 703257)),
        ),
        migrations.AlterField(
            model_name='addblog',
            name='btime',
            field=models.TimeField(default=datetime.datetime(2020, 7, 3, 23, 44, 29, 703237)),
        ),
    ]
