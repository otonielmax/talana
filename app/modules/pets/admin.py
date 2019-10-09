from django.contrib import admin

from modules.users.models import Users
from modules.votes.models import Votes

# Register your models here.
admin.site.register(Users)
admin.site.register(Votes)
