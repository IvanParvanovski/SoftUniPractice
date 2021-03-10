from django.urls import path

from testing.views import index

urlpatterns = (
    path('', index, name='profiles'),
)
