# Generated by Django 4.0.2 on 2022-03-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0086_remove_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmatch',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
