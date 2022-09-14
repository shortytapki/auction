from importlib.metadata import requires
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(
        'Listing', on_delete=models.CASCADE, blank=False)


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=30, blank=True, default="")
    starting_bid = models.IntegerField(default=0)
    image_url = models.URLField(max_length=500, blank=True, default="")
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
