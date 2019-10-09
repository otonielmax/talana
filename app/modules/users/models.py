from django.db import models

# Create your models here.
class Users(models.Model):
    alias = models.CharField(max_length=8)        