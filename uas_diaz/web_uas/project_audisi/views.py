from django.shortcuts import render
from .models import Kompetisi  # Import the Kompetisi model
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def index(request):
    competitions = Kompetisi.objects.all()  # Fetch all competitions
    return render(request, 'index.html', {'competitions': competitions})  # Pass context to the template

def daftar(request):
    return render(request, 'daftar.html')

def daftar(request):
    return render(request, 'karya.html')

def kompetisi(request):
    return render(request, 'kompetisi.html')
