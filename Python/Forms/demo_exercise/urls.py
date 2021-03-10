from django.urls import path
from demo_exercise.views import index, index_bootstrap, create_demo_exercise_form

urlpatterns = [
    path('', index, name='main page'),
    path('bootstrap', index_bootstrap),
    path('create/', create_demo_exercise_form, name='create demo_exercise_form'),
]
