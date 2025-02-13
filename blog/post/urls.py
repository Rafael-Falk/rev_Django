from django.urls import path
from . import views

urlpatterns = [
    path('teste1/', views.timelineView, name='post_list'),
    path('teste2/', views.index, name='post_list')
]   