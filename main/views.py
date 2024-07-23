from django.shortcuts import render
# Create your views here.

# views.py

from django.shortcuts import render
from .models import Page

def home(request):
    page = Page.objects.get(title='Home')
    return render(request, 'home.html', {'content': page.content})

def boats(request):
    page = Page.objects.get(title='Boats')
    return render(request, 'boats.html', {'content': page.content})

def cruises(request):
    page = Page.objects.get(title='Cruises')
    return render(request, 'cruises.html', {'content': page.content})

def profile(request):
    page = Page.objects.get(title='Profile')
    return render(request, 'profile.html', {'content': page.content})