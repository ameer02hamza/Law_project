# Generated by Django 3.0.6 on 2020-07-03 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20200703_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 22, 30, 24, 301333)),
        ),
        migrations.AlterField(
            model_name='addblog',
            name='btime',
            field=models.TimeField(default=datetime.datetime(2020, 7, 3, 22, 30, 24, 301315)),
        ),
    ]
