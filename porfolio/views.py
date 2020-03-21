from django.shortcuts import render
from .models import Project

def home(request):
    theproject=Project.objects.all()
    return render(request,"portfolio/home.html", {"project": theproject})
