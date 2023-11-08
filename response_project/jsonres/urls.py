from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainres, name="main"),
    path("json/", views.jsonres, name="jsonres"),
    path("html/", views.htmlres, name="htmlres"),
    path("text/", views.textres, name="textres"),
]
