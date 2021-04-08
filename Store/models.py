from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    preview_img = models.ImageField(default = 'default.png', upload_to="media/productprev/")
    pdf = models.FileField(default = 'default.png', upload_to="media/pdfs/")
    date = models.DateTimeField(default=datetime.now, blank=True)
