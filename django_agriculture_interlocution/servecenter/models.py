from typing import Any
from django.db import models

# Create your models here.

class ServeINfo(models.Model):
    image=models.ImageField(upload_to='services/', blank=True, null=True)
    serial =models.IntegerField()
    title=models.CharField(max_length=10)
    
    info=models.TextField()
    

    def __init__(self):
        return self.title
