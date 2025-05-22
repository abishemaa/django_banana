from django.shortcuts import render
from django import forms


tasks = ["Task 1", "Task 2", "Task 3"]

# Create your views here.
def index(request):
    # Render the index.html template
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Add a new task:
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })