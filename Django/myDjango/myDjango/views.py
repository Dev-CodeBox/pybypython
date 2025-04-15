from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World")
    return render(request, "website/home.html")

def about(request):
    # return HttpResponse("Hello World")
    return render(request, "website/about.html")
