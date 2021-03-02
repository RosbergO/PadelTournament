import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# TODO : Gör klart friends.

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='request_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    created = models.DateTimeField(datetime.datetime.now())
    accepted = models.BooleanField(default=False)


class Friendship(models.Model):
    user = models.OneToOneField(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', symmetrical=True)
