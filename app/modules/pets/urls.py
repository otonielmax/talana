from django.conf.urls import url

from modules.pets.views import home, create

urlpatterns = [
    url(r'^$', home),
    url(r'^create$', create),
]
