from django.db import models

from modules.users.models import Users
from modules.pets.models import Pets

# Create your models here.
class Votes(models.Model):
    users = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    pets = models.ForeignKey(Pets, null=True, blank=True, on_delete=models.CASCADE)