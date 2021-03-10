from django.contrib import admin
from main_app.models import todo

# Register your models here.
admin.site.register(todo.Todo)
