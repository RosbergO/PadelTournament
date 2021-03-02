from django.urls import path
from Tournament.views import *

urlpatterns = [
    path('teams/', TeamList.as_view()),
    path('teams/test', TeamList.as_view()),
    path('teams/<int:pk>/', TeamDetail.as_view()),
    path('tournaments/', TournamentList.as_view()),
    path('tournaments/<int:pk>/', TournamentDetail.as_view()),
    path('matches/', MatchList.as_view()),
    path('matches/<int:pk>/', TeamDetail.as_view()),
]