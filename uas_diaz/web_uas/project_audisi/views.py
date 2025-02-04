from django.shortcuts import render
from .models import Kompetisi  # Import the Kompetisi model
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def daftar(request):
    return render(request, 'daftar.html')

def karya(request):
    return render(request, 'karya.html')

def kompetisi(request):
    return render(request, 'kompetisi.html')

def index(request):
    return render(request, 'index.html')
