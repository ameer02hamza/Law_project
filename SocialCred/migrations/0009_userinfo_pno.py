# Generated by Django 3.0.6 on 2020-07-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialCred', '0008_auto_20200703_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='pno',
            field=models.BigIntegerField(default=0),
        ),
    ]
