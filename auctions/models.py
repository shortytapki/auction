from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=30, null=True)
    starting_bid = models.IntegerField(default=0)
    image_url = models.URLField(max_length=500, null=True)
