# Generated by Django 4.0.2 on 2022-03-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0023_alter_buisness_buisness_owner_alter_buisness_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisness',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
