# Generated by Django 3.0.6 on 2020-07-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lawyers', '0002_auto_20200713_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='ratings',
        ),
    ]
