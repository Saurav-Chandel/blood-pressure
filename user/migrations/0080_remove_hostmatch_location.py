# Generated by Django 4.0.2 on 2022-03-25 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0079_alter_hostinvitation_user_invited_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostmatch',
            name='location',
        ),
    ]
