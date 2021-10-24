from django.db import models

# Create your models here.

class UsernameInstagramUser(models.Model):
    username = models.CharField(max_length=50)