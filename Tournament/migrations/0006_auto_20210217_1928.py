# Generated by Django 3.1.6 on 2021-02-17 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tournament', '0005_auto_20210215_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='number_of_teams',
        ),
        migrations.AddField(
            model_name='team',
            name='member',
            field=models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='first_team_score',
            field=models.IntegerField(choices=[(0, '0'), (15, '15'), (30, '30'), (40, '40'), (50, 'GAME')]),
        ),
        migrations.AlterField(
            model_name='game',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_name', to='Tournament.match'),
        ),
        migrations.AlterField(
            model_name='game',
            name='second_team_score',
            field=models.IntegerField(choices=[(0, '0'), (15, '15'), (30, '30'), (40, '40'), (50, 'GAME')]),
        ),
        migrations.AlterField(
            model_name='match',
            name='first_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_team', to='Tournament.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='second_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_team', to='Tournament.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_name', to='Tournament.tournament'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
