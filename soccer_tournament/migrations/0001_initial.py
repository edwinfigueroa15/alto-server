# Generated by Django 5.0.6 on 2024-06-11 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('position', models.CharField(max_length=2)),
                ('points', models.CharField(max_length=3)),
                ('matches_won', models.CharField(max_length=2)),
                ('lost_matches', models.CharField(max_length=2)),
                ('tied_matches', models.CharField(max_length=2)),
                ('goals_favor', models.CharField(max_length=2)),
                ('goals_against', models.CharField(max_length=2)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.CharField(max_length=2)),
                ('goals_team_two', models.CharField(max_length=2)),
                ('status', models.CharField(max_length=30)),
                ('data_start', models.DateField()),
                ('created', models.DateField(auto_now_add=True)),
                ('team_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_one', to='soccer_tournament.team')),
                ('team_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_two', to='soccer_tournament.team')),
            ],
        ),
    ]
