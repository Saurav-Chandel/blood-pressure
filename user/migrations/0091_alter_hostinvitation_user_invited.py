# Generated by Django 4.0.2 on 2022-03-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0090_alter_hostinvitation_user_invited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinvitation',
            name='user_invited',
            field=models.ManyToManyField(related_name='user_invited_friendrequest', to='user.FriendRequest'),
        ),
    ]
