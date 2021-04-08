from django.db import models
from datetime import datetime

# Create your models here.
class movies(models.Model):
    title = models.CharField(max_length=200)
    display_img = models.ImageField(default='default.png', upload_to="media/gallery/movies/")
    date = models.DateTimeField(default=datetime.now, blank=True)

class behind_the_scene(models.Model):
    title = models.CharField(max_length=200)
    display_img = models.ImageField(default='default.png', upload_to="media/gallery/scenes/")
    date = models.DateTimeField(default=datetime.now, blank=True)
