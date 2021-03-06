# Generated by Django 4.0.2 on 2022-02-28 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0009_remove_buisness_profile_buisness_buisness_owner'),
        ('user', '0050_usertype_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='type_name',
        ),
        migrations.AddField(
            model_name='user',
            name='user_buisness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buisness.buisness'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_type', to='user.usertype'),
        ),
    ]
