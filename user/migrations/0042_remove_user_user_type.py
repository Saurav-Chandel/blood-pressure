# Generated by Django 4.0.2 on 2022-02-28 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_rename_type_usertype_role_alter_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
