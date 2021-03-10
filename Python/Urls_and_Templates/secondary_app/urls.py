from django.urls import path
from secondary_app import views

urlpatterns = [
    path('', views.index),
]
