# Generated by Django 4.0.2 on 2022-03-29 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0088_remove_hostmatch_lat_remove_hostmatch_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostmatch',
            name='pincode',
        ),
    ]