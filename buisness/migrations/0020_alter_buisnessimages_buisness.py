# Generated by Django 4.0.2 on 2022-03-10 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0019_buisnessimages_remove_buisness_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisnessimages',
            name='buisness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buisness_images', to='buisness.buisness'),
        ),
    ]