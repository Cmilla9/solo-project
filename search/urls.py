from django.conf.urls import url
from django.contrib import admin
from .views import searchfood

urlpatterns = [
    url(r'^$', searchfood, name='searchfood'),
]