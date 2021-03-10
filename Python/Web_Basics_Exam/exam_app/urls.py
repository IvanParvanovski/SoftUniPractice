from django.urls import path

from exam_app.views.home_page import index
from exam_app.views.recipe_crud import recipe_create,\
                                       recipe_edit,\
                                       recipe_delete,\
                                       recipe_details

urlpatterns = (
    path('', index, name='home page'),
    path('create', recipe_create, name='recipe create'),
    path('edit/<int:pk>', recipe_edit, name='recipe edit'),
    path('delete/<int:pk>', recipe_delete, name='recipe delete'),
    path('details/<int:pk>', recipe_details, name='recipe details'),
)
