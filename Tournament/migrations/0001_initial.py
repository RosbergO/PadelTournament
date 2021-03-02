# Generated by Django 3.1.3 on 2021-02-11 12:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('numberOfTeams', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('firstTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firstTeam', to='Tournament.team')),
                ('secondTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondTeam', to='Tournament.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstTeamScore', models.IntegerField(choices=[(0, 'ZERO_POINTS'), (15, 'ONE_POINT'), (30, 'TWO_POINTS'), (40, 'THREE_POINTS'), (50, 'GAME')])),
                ('secondTeamScore', models.IntegerField(choices=[(0, 'ZERO_POINTS'), (15, 'ONE_POINT'), (30, 'TWO_POINTS'), (40, 'THREE_POINTS'), (50, 'GAME')])),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tournament.match')),
            ],
        ),
    ]
