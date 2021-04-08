from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Profile',null = True)
    stripeCustomerId = models.CharField(max_length=255,default = 'a')
    stripeSubscriptionId = models.CharField(max_length=255,default = 'a')
    paid = models.BooleanField(default=False)