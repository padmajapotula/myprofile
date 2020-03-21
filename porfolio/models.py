from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    img=models.ImageField(upload_to='myprofiles/portfolio')
    url=models.URLField(blank=True)