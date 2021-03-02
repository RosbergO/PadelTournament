from random import randint

from django.test import TestCase
from factory.django import DjangoModelFactory
from Tournament.models import *
from model_bakery import baker
from model_bakery.recipe import Recipe, seq


class TestPool(TestCase):
    def test_round_robin(self):
        self.teams = baker.make('Team', _quantity=4)
        self.pool = baker.make('Pool', teams=self.teams)
        self.pool.generate_round_robin()
        print(self.pool.match_set.all())


class TestTournament(TestCase):
    def setUp(self):
        self.teams = baker.make('Team', _quantity=8)
        self.tournament = baker.make('Tournament', teams=self.teams)

    def test_generate_pools(self):
        self.teams = baker.make('Team', _quantity=8)
        self.tournament = baker.make('Tournament', teams=self.teams)
        self.tournament.generate_random_pools(2)


class TestMatch(TestCase):
    def setUp(self):
        self.first_team = baker.make('Team', name='Team1')
        self.second_team = baker.make('Team', name='Team2')

    def test_winner_team1(self):
        self.match = baker.make('Match',
                                first_team=self.first_team,
                                second_team=self.second_team,
                                first_team_score=5,
                                second_team_score=2,
                                round_number=1)
        self.assertEqual(self.match.winner(), self.first_team)

    def test_winner_team2(self):
        self.match = baker.make('Match',
                                first_team=self.first_team,
                                second_team=self.second_team,
                                first_team_score=2,
                                second_team_score=5,
                                round_number=1)
        self.assertEqual(self.match.winner(), self.second_team)
