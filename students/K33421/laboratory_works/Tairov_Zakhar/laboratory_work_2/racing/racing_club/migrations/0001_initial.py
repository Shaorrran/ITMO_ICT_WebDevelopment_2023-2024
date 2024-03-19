# Generated by Django 5.0.3 on 2024-03-19 17:24

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Race',
                'verbose_name_plural': 'Races',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comment text')),
                ('comment_type', models.CharField(choices=[('suggests', 'Suggestions'), ('races', 'Races'), ('complaints', 'Complaints'), ('other', 'Misc')], max_length=32, verbose_name='Comment type')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Comment rating')),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date and time posted')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Poster')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racing_club.race', verbose_name='Race')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(null=True, verbose_name='Full name')),
                ('biography', models.TextField(verbose_name='Racer biography')),
                ('num_of_races', models.IntegerField(default=0, verbose_name='Number of races')),
                ('car_name', models.TextField(null=True, verbose_name='Car name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='racing_club.team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Racer',
                'verbose_name_plural': 'Racers',
            },
        ),
        migrations.CreateModel(
            name='RaceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racing_club.race', verbose_name='Race')),
                ('racer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racing_club.racer', verbose_name='Racer')),
            ],
            options={
                'verbose_name': 'Race participation',
                'verbose_name_plural': 'Race participations',
            },
        ),
        migrations.AddField(
            model_name='race',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='racing_club.team', verbose_name='Winner'),
        ),
    ]
