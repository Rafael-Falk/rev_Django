from django.shortcuts import render
from django.http import HttpResponse
from .models import Timeline
# Create your views here.

def timelineView(request):
    
    posts = Timeline.objects.filter(id='1')
    for post in posts:
        print(f">>> {post} <<<")
    return HttpResponse("ta feito")

def index(request):
    posts = Timeline.objects.all()
    return render(request,'template.html', {"dados": posts})