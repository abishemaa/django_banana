import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    # Render the index.html template
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.day == 1 and now.month == 1,
    })