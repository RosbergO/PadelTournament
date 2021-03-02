from Tournament import models
from factory.django import DjangoModelFactory
from factory import SubFactory


class TeamFactory(DjangoModelFactory):
    class Meta:
        model = models.Team

    name = "Best Team"


class TournamentFactory(DjangoModelFactory):
    class Meta:
        model = models.Tournament


class BracketFactory(DjangoModelFactory):
    class Meta:
        models = models.Bracket

    tournament = SubFactory(TournamentFactory)
