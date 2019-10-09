from django.db import models

from modules.users.models import Users

# Create your models here.
class Pets(models.Model):
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    picture = models.FileField()
