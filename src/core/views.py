from django.shortcuts import render
from django.http import HttpResponse
from . import models 

# Create your views here.

def home(request):
    return HttpResponse("everything ok")