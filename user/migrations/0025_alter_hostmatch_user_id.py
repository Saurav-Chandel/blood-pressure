# Generated by Django 4.0.2 on 2022-02-16 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_remove_teamscore_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmatch',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostmatch_profile', to='user.profile'),
        ),
    ]
