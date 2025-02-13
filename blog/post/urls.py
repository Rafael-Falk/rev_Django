from django.urls import path
from . import views

urlpatterns = [
    path('', views.timelineView, name='post_list'),
]   