from django.urls import path
from lobby import views

urlpatterns = [
    path('', views.index),
]

