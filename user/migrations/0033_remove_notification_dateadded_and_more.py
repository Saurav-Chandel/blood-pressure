# Generated by Django 4.0.2 on 2022-02-18 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='DateAdded',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='RefferalCode',
        ),
    ]
