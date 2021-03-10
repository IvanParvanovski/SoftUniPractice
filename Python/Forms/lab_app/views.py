from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from lab_app.forms.lab import LabForm
from lab_app.models.lab import Lab


def index(req, form=None, form_action='create lab_form', pk=None):
    if not form:
        form = LabForm()

    context = {
        'lab_users': Lab.objects.all(),
        'lab_form': form,
        'form_action': form_action,
        'pk': pk,
    }

    return render(req, 'lab_app_tmp/index.html', context=context)


@require_POST
def create_lab_form(req):
    form = LabForm(req.POST)

    if form.is_valid():
        new_user = Lab(name=form.cleaned_data['name'],
                       age=form.cleaned_data['age'],
                       email=form.cleaned_data['email'],
                       password=form.cleaned_data['password'],
                       text=form.cleaned_data['text'])

        new_user.save()
        return redirect('main page')

    return index(req, form)


def edit_user(req, pk):
    user = Lab.objects.get(pk=pk)

    if req.method == 'GET':
        form = LabForm(initial=user.__dict__)
        return index(req, form, 'edit user', pk=pk)

    form = LabForm(req.POST)
    if form.is_valid():
        user.name = form.cleaned_data['name']
        user.age = form.cleaned_data['age']
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.text = form.cleaned_data['text']
        user.save()

    return index(req, form)


def delete_user(req):
    pass

