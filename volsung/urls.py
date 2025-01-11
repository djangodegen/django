from django.urls import path

from . import views

app_name = "v"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("us", views.us, name="us"),
    path("test", views.test, name="test"),
]
