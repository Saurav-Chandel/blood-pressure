# Generated by Django 4.0.2 on 2022-02-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0052_alter_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_buisness',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
