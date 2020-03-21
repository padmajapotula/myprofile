from django.db import models
from datetime import datetime

class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now())
    
