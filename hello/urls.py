from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("faiz", views.faiz, name="faiz"),
    path("<str:name>", views.greet, name="greet")
]