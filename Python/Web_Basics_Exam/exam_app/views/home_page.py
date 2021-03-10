from django.shortcuts import render

from exam_app.models.recipe import Recipe


def index(req):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(req, 'index.html', context=context)
