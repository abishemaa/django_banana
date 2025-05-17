from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'banana/index.html')

def fruits(request, name):
    return render(request, "banana/fruits.html", {
        "name": name.capitalize()
    })