# Generated by Django 4.0.2 on 2022-03-01 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0010_alter_buisness_short_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisness',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buisness.service'),
        ),
    ]
