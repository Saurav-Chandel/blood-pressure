# Generated by Django 4.0.2 on 2022-03-24 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0072_alter_friendrequest_options_friendrequest_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friendrequest',
            options={'ordering': ['-date_added']},
        ),
        # migrations.RemoveField(
        #     model_name='friendrequest',
        #     name='created',
        # ),
        migrations.AddField(
            model_name='friendrequest',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
