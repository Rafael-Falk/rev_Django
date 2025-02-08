from django.contrib import admin

# Register your models here.

from .models import Timeline

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display=['nome', 'data_publicacao', 'texto']
    search_fields=['nome']

