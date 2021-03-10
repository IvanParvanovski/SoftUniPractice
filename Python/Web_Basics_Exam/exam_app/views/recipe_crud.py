from django.shortcuts import redirect, render

from exam_app.forms.recipe import RecipeCreateForm, DisabledRecipeForm
from exam_app.models.recipe import Recipe
from exam_app.views.shared import visualise_view


def recipe_create(req):
    if req.method == 'GET':
        form = RecipeCreateForm()
        return visualise_view(req, form, 'create.html')
    else:
        form = RecipeCreateForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

        return visualise_view(req, form, 'create.html')


def recipe_edit(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    if req.method == 'GET':
        form = RecipeCreateForm(instance=recipe)
        return visualise_view(req, form, 'edit.html')
    else:
        form = RecipeCreateForm(req.POST,
                                instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('home page')

        return visualise_view(req, form, 'edit.html')


def recipe_delete(req, pk):
    recipe = Recipe.objects.get(pk=pk)

    if req.method == 'GET':
        form = DisabledRecipeForm(instance=recipe)
        return visualise_view(req, form, 'delete.html')
    else:
        recipe.delete()
        return redirect('home page')


def recipe_details(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(', ')
    }

    return render(req, 'details.html', context=context)
