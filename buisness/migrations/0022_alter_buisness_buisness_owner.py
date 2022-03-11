# Generated by Django 4.0.2 on 2022-03-10 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buisness', '0021_remove_buisness_buisness_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisness',
            name='buisness_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buisness_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]