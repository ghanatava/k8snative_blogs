from django.shortcuts import render
from .models import *

def index(request):
    return render(request,"blogs/index.html",{
        "posts" : Post.objects.all(),"title":"bolgs",
    })


def about(request):
    return render(request,"blogs/about.html",{
        "title":"about"
    })
