from django.urls import path

from main_app.views.home_page import home_page
from main_app.views.expense import create_expense,\
                                   edit_expense,\
                                   delete_expense

urlpatterns = (
    path('', home_page, name='home page'),
    path('create', create_expense, name='expense create'),
    path('edit/<int:pk>', edit_expense, name='expense edit'),
    path('delete:<int:pk>', delete_expense, name='expense delete'),
)
