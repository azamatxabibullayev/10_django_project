from django.urls import path
from cartoons.views import cartoons

urlpottenrs = [
    path('cartoons', cartoons)
]
