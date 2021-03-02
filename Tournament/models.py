import datetime
import pkgutil
from random import shuffle
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models import Count
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)
    member = models.ManyToManyField('auth.User', related_name='member')

    def __str__(self):  # Returns field name
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team)
    round_number = models.IntegerField(default=1)

    # number_of_teams = Team.objects.get(id)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def generate_random_pools(self, number_of_pools):
        teams = self.teams.all().order_by('?')
        pools = list(self.split_evenly(teams, number_of_pools))
        for pool in pools:
            this_pool = Pool.objects.create(tournament=self)
            for team in pool:
                this_pool.teams.add(team)

    def split_evenly(self, a, n):
        """Returns an evenly distributed list of lists with teams"""
        k, m = divmod(len(a), n)
        return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

#TODO Finish implementation of generate_bracket().
    def generate_bracket(self, teams):
        shuffle(teams)
        initial_matches = []
        match_round = 1
        for team in teams:
            match = Match(first_team=teams.pop(), second_team=teams.pop(), round_number=match_round)
            initial_matches.append(match)
        match_round += 1
        return initial_matches


# TODO FIX ROUND ROBIN

class Pool(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    def generate_round_robin(self):
        teams = self.teams.all()
        # number_of_matches = (teams.count() / 2) * (teams.count() - 1)
        for i in range(len(teams) - 1):
            for n in range(i + 1, len(teams)):
                Match.objects.create(first_team=teams[i], second_team=teams[n], round_number=1, pool=self)

    def __str__(self):
        return str(self.teams.all())


class Match(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_team')
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='second_team')
    round_number = models.IntegerField()
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    first_team_score = models.PositiveSmallIntegerField(default=0)
    second_team_score = models.PositiveSmallIntegerField(default=0)

    # tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_name')
    def winner(self):
        if self.first_team_score > self.second_team_score:
            return self.first_team
        return self.second_team

    def __str__(self):
        return '{} vs {}'.format(self.first_team, self.second_team)


