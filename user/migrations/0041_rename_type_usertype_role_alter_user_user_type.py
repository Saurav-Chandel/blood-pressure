# Generated by Django 4.0.2 on 2022-02-28 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_alter_usertype_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertype',
            old_name='type',
            new_name='role',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertype'),
        ),
    ]
