# Generated by Django 4.0.2 on 2022-02-10 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_buisness_buisness_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team1players',
            name='host_match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_player_1', to='user.hostmatch'),
        ),
        migrations.AlterField(
            model_name='team2players',
            name='host_match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_player_2', to='user.hostmatch'),
        ),
    ]
