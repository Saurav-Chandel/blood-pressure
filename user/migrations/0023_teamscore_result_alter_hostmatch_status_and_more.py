# Generated by Django 4.0.2 on 2022-02-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamscore',
            name='result',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hostmatch',
            name='status',
            field=models.CharField(blank=True, choices=[('Initiated', 'Initiated'), ('Completed', 'Completed'), ('Cancel', 'cancel')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Buisness',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
