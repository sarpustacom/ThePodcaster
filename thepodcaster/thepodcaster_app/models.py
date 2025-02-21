from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Show(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=160)
    cover_url = models.URLField()
    keywords = models.CharField(max_length=160)
    copyright = models.CharField(max_length=160)
    description = models.CharField(max_length=250)
    language = models.CharField(max_length=10)
    explicit = models.BooleanField(default=False)
    pubDate = models.DateTimeField(auto_now_add=True)

class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    pubDate = models.DateTimeField(auto_now_add=True)
    media_url = models.URLField()
    media_size = models.CharField(max_length=15)
    media_type = models.CharField(max_length=45)
    duration = models.CharField(max_length=15)
    guid = models.UUIDField()
    explicit = models.BooleanField(default=False)
    description = models.CharField(max_length=250)