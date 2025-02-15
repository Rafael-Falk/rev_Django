from django.contrib import admin

# Register your models here.

from .models import Perfil, User

@admin.register(Perfil,User)
class registro_perfil(admin.ModelAdmin):
    list_display=['nome', 'sobrenome', 'data_nascimento', 'sexo','email','telefone', 'user' ]