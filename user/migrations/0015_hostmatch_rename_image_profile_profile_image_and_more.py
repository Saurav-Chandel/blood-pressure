# Generated by Django 4.0.2 on 2022-02-09 04:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_contactus_user_id_alter_profile_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('select_mode', models.CharField(blank=True, choices=[('public', 'public'), ('private', 'private')], max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('Initiated', 'Initiated'), ('Completed', 'Completed'), ('InCompleted', 'InCompleted')], max_length=200, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='matchhost',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='matchplayed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='matchwon',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='TeamScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('team1_player_score', models.IntegerField()),
                ('team2_player_score', models.IntegerField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('host_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_score', to='user.hostmatch')),
            ],
        ),
        migrations.CreateModel(
            name='Team2Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('host_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.hostmatch')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Team1Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('host_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.hostmatch')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PlayersRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('host_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.hostmatch')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.AddField(
            model_name='hostmatch',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.CreateModel(
            name='HostInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Sent', 'Sent'), ('Decline', 'Decline'), ('Attend', 'Attend')], max_length=200, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('hostmatch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostmatch', to='user.hostmatch')),
                ('user_invited', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='user.profile')),
            ],
        ),
    ]