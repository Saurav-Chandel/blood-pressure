# Generated by Django 4.0.2 on 2022-03-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0011_alter_buisness_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buisness',
            name='service',
        ),
        migrations.AddField(
            model_name='buisness',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, to='buisness.Service'),
        ),
    ]
