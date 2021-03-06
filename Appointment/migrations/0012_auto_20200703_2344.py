# Generated by Django 3.0.6 on 2020-07-03 23:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Appointment', '0011_auto_20200703_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='nusr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointmentform',
            name='adate',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 23, 44, 29, 704172)),
        ),
        migrations.AlterField(
            model_name='appointmentform',
            name='atime',
            field=models.TimeField(default=datetime.datetime(2020, 7, 3, 23, 44, 29, 704187)),
        ),
        migrations.AlterField(
            model_name='notify',
            name='ndate',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 23, 44, 29, 705275)),
        ),
        migrations.AlterField(
            model_name='notify',
            name='ntime',
            field=models.TimeField(default=datetime.datetime(2020, 7, 3, 23, 44, 29, 705290)),
        ),
    ]
