# Generated by Django 3.0.6 on 2020-07-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialCred', '0007_auto_20200511_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='speciality',
            field=models.CharField(default='', max_length=255),
        ),
    ]
