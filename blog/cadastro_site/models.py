from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Perfil(models.Model):
    nome= models.CharField(max_length=20)
    sobrenome= models.CharField(max_length=20)
    data_nascimento= models.DateTimeField
    sexo= models.
    email= models.EmailField
    telefone= models.CharField(max_length=15)
class User(models.Model):
    user= models.OneToOneField(Perfil)
    
    
    
    