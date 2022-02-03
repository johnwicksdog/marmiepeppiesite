from django.shortcuts import render
from .models import Project, Cat

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def cats(request):
    cats = Cat.objects.all()
    return render(request, 'portfolio/cats.html', {'cats':cats })

def gallery(request):
    return render (request, 'portfolio/gallery.html')
