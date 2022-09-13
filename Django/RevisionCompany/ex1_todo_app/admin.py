from django.contrib import admin

# Register your models here.
from ex1_todo_app.models import TodoList

admin.site.register(TodoList)
