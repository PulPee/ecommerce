# Generated by Django 2.1.2 on 2018-11-20 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activationcode',
            old_name='user_id',
            new_name='user',
        ),
    ]
