from django.urls import path

from pythons_auth.views import login_user, logout_user, register_user

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user')
)