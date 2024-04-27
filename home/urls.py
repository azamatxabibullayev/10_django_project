from django.urls import path
from home.views import home

urlpotterns = [
    path('home', home)
]
