from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from demo_exercise.forms import DemoExerciseForm, DemoExerciseFormFull
from demo_exercise.models.demo_ex import Demo


def index_bootstrap(req):
    context = {
        'demo_exercise_form': DemoExerciseForm()
    }

    return render(req, 'demo_exercise_tmp/index_bootstrap.html', context=context)


def index(req, form=None):
    if not form:
        form = DemoExerciseFormFull()

    context = {
        'demo_exercise_form': form,
    }

    return render(req, 'demo_exercise_tmp/index.html', context=context)


@require_POST
def create_demo_exercise_form(req):
    form = DemoExerciseFormFull(req.POST)

    if form.is_valid():
        # d = Demo(name=form.cleaned_data['name'])
        demo = Demo(name=form.cleaned_data['name'],
                    age=form.cleaned_data['age'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    text=form.cleaned_data['text'],
                    size=form.cleaned_data['size'])
        demo.save()
        return redirect('main page')

    return index(req, form)
