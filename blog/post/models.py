from django.db import models
from django.utils import timezone

# Create your models here.

class Timeline(models.Model):
    nome= models.CharField(max_length=30)
    data_publicacao = models.DateTimeField(default=timezone.now)
    texto=models.CharField(max_length=300)
    
    