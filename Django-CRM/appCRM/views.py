from django.shortcuts import render
from .models import *

def home(recuest):
    return render(recuest, 'index.html')