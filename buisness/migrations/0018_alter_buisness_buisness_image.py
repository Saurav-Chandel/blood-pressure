# Generated by Django 4.0.2 on 2022-03-08 10:44

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0017_alter_buisness_buisness_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisness',
            name='buisness_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media.root/buisness_images2022-03-08'), upload_to=''),
        ),
    ]
