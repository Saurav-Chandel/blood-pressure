# Generated by Django 4.0.2 on 2022-03-11 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0028_alter_buisnessimages_buisness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisnessimages',
            name='buisness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buisness.buisness'),
        ),
    ]
