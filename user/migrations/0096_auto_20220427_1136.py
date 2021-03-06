# Generated by Django 3.2.12 on 2022-04-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0095_hostmatch_player_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostmatch',
            name='player_counts',
        ),
        migrations.AddField(
            model_name='hostmatch',
            name='latitude',
            field=models.FloatField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='hostmatch',
            name='longitude',
            field=models.FloatField(blank=True, max_length=500, null=True),
        ),
    ]
