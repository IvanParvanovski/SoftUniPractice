from django.urls import path

from lab_app.views import index, create_lab_form, edit_user, delete_user

urlpatterns = [
    path('', index, name='main page'),
    path('create/', create_lab_form, name='create lab_form'),
    path('edit/<int:pk>', edit_user, name='edit user'),
    path('delete/<int:pk>', delete_user, name='delete user')
]
