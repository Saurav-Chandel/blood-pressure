# Generated by Django 4.0.2 on 2022-02-14 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_user_is_active'),
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suspend_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
