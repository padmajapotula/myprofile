from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    theblog=Blog.objects.all()
    return render(request,'blog/blog.html',{"blog":theblog})
