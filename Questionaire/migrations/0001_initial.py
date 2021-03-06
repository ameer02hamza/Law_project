# Generated by Django 3.0.6 on 2020-07-16 14:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SocialCred', '0009_userinfo_pno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('question', models.TextField(default='')),
                ('ptime', models.TimeField(default=django.utils.timezone.now)),
                ('pdate', models.DateField(default=django.utils.timezone.now)),
                ('uprof', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='SocialCred.UserInfo')),
            ],
        ),
    ]
