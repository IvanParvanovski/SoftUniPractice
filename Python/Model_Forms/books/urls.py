from django.urls import path

from books import views

urlpatterns = [
    path('', views.index, name='books index'),
    path('create/', views.create_form, name='create'),
    path('edit/<int:pk>', views.edit_form, name='edit'),
]
