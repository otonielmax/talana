from django import forms
from django.forms import ModelForm

from modules.pets.models import Pets

class PetsForm(ModelForm):
    class Meta:
        model = Pets
        fields = ['user', 'name', 'picture']