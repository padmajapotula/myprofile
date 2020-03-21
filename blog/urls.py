from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<int:blog_id>', views.details, name="details"),
]