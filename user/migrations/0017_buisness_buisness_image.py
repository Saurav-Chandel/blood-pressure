# Generated by Django 4.0.2 on 2022-02-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_service_profile_contact_number_buisness'),
    ]

    operations = [
        migrations.AddField(
            model_name='buisness',
            name='buisness_image',
            field=models.ImageField(blank=True, null=True, upload_to='buisness_image'),
        ),
    ]