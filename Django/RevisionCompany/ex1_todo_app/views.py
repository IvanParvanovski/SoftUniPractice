from django.shortcuts import render
from ex1_todo_app.models import TodoList

# Create your views here.


def index(req):
    tasks = TodoList.objects.all()

    context = {
        'tasks': tasks,
    }

    return render(req, 'index.html', context=context)
