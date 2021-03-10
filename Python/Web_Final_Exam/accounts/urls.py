from django.urls import path

from accounts.views import UserSignUp, sign_out_view, UserSignIn, Profile, ProfileUpdate, delete_profile_view

urlpatterns = (
    path('<int:pk>', Profile.as_view(), name='profile'),
    path('profile_edit/<int:pk>', ProfileUpdate.as_view(), name='edit profile'),
    path('delete_profile/<int:pk>', delete_profile_view, name='delete profile'),

    path('sign_up/', UserSignUp.as_view(), name='user sign up'),
    path('sign_out/', sign_out_view, name='user sign out'),
    path('sign_in/', UserSignIn.as_view(), name='user sign in'),
)
