# Generated by Django 4.0.2 on 2022-02-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0045_alter_usertype_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]