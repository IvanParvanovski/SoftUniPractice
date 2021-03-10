from django.urls import path

from profile_app import views

urlpatterns = (
    path('', views.profile_page, name='profile'),
    path('edit', views.profile_edit, name='profile edit'),
    path('delete', views.profile_delete, name='profile delete'),
)
