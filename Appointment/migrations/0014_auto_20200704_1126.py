# Generated by Django 3.0.6 on 2020-07-04 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0013_auto_20200703_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentform',
            name='adate',
            field=models.DateField(default=datetime.datetime(2020, 7, 4, 11, 26, 53, 844147)),
        ),
        migrations.AlterField(
            model_name='appointmentform',
            name='atime',
            field=models.TimeField(default=datetime.datetime(2020, 7, 4, 11, 26, 53, 844163)),
        ),
        migrations.AlterField(
            model_name='notify',
            name='ndate',
            field=models.DateField(default=datetime.datetime(2020, 7, 4, 11, 26, 53, 845265)),
        ),
        migrations.AlterField(
            model_name='notify',
            name='ntime',
            field=models.TimeField(default=datetime.datetime(2020, 7, 4, 11, 26, 53, 845281)),
        ),
    ]
