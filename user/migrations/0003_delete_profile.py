# Generated by Django 4.0.2 on 2022-02-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
