from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def cartoons(request):
    return HttpResponse('ALL ABOUT CARTOONS !!')
