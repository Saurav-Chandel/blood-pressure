# Generated by Django 4.0.2 on 2022-03-24 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0073_alter_friendrequest_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='created',
        ),
    ]
