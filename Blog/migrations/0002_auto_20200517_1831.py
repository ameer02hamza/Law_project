# Generated by Django 2.2.12 on 2020-05-17 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2020, 5, 17, 18, 31, 20, 112252)),
        ),
        migrations.AlterField(
            model_name='addblog',
            name='btime',
            field=models.TimeField(default=datetime.datetime(2020, 5, 17, 18, 31, 20, 112229, tzinfo=utc)),
        ),
    ]
