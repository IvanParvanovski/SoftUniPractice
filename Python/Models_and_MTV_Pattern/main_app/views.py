from django.shortcuts import render
from main_app.models.person import Person
from main_app.models.todo import Todo


def index(req):
    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(req, './main_app_tmp/index.html', context=context)

# Create your views here.
