# Generated by Django 3.0.6 on 2020-07-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialCred', '0009_userinfo_pno'),
        ('Questionaire', '0002_auto_20200716_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='uprof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialCred.UserInfo'),
        ),
    ]
