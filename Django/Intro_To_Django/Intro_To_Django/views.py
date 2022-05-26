from django.shortcuts import render
from app_models.person import Person

p = Person


def index(req):
    context = {
        'app_name': 'my_first_app'
    }

    return render(req, 'index.html', context=context)


