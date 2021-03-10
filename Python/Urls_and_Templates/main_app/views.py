from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


def index(req):
    title = "Url's and Templates"
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
        # 'users': list()
    }

    return render(req, './main_app/index.html', context)
