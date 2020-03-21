from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    theblog=Blog.objects.all()
    return render(request,'blog/blog.html',{"blog":theblog})

def details(request,blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/details.html',{"blog":blog})
