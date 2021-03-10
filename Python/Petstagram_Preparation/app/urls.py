from django.urls import path

from app.views.home_page import landing_page
from app.views.pet import pet_create,\
                          pet_delete,\
                          pet_list,\
                          pet_detail,\
                          pet_like,\
                          pet_edit

urlpatterns = (
    path('', landing_page, name='landing page'),

    path('pets', pet_list, name='pet list'),
    path('pets/details/<int:pk>', pet_detail, name='pet detail'),
    path('pets/like/<int:pk>', pet_like, name='pet like'),

    path('pets/edit/<int:pk>', pet_edit, name='pet edit'),
    path('pets/create', pet_create, name='pet create'),
    path('pets/delete/<int:pk>', pet_delete, name='pet delete'),

)
