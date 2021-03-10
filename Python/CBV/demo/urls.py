from django.urls import path
from django.views.generic import TemplateView

from demo.views import IndexView, IndexTemplateView, PetListView, PetDetails

urlpatterns = (
   path('', IndexView.as_view()),
   path('1', IndexTemplateView.as_view()),
   path('2', TemplateView.as_view(template_name='index.html')),
   path('list/', PetListView.as_view(), name='pets page'),
   path('details/<int:pk>', PetDetails.as_view(), name='pet details'),
)
