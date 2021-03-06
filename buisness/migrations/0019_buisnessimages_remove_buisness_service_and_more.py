# Generated by Django 4.0.2 on 2022-03-10 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buisness', '0018_alter_buisness_buisness_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuisnessImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buisness_images', models.ImageField(upload_to='buisnessimages')),
            ],
        ),
        migrations.RemoveField(
            model_name='buisness',
            name='service',
        ),
        migrations.AlterField(
            model_name='buisness',
            name='buisness_image',
            field=models.ImageField(blank=True, null=True, upload_to='buisness_image'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='buisnessimages',
            name='buisness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buisness.buisness'),
        ),
    ]
