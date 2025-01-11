from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.


# Make sure to add app VolsungConfig to
# settings.py config file
def index(request):
    # return HttpResponse("Hello world! Welcome to the index page of my django app!")
    return render(request, "volsung/index.html")


def about(request):
    # return HttpResponse("This is the about page for my django app!")
    return render(request, "volsung/about.html")


def us(request):
    return HttpResponse("New page for our application")


def test(request):
    return HttpResponse("Test url")
