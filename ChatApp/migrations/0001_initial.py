# Generated by Django 3.0.6 on 2020-07-19 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SocialCred', '0009_userinfo_pno'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesreciever', to='SocialCred.UserInfo')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgsender', to='SocialCred.UserInfo')),
            ],
        ),
    ]
