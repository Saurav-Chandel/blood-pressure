# Generated by Django 4.0.2 on 2022-03-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0024_alter_buisness_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisnessimages',
            name='buisness_images',
            field=models.ImageField(blank=True, null=True, upload_to='buisnessimages'),
        ),
    ]