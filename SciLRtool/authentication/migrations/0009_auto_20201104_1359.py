# Generated by Django 3.1.2 on 2020-11-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_profile_public_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dropbox_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mendeley_token',
        ),
    ]
