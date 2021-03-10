from django.shortcuts import render, redirect

from main_app.common.budget import calculate_left_budget
from main_app.models.expense import Expense
from main_app.views.shared import visualise_view
from profile_app.forms.profile import ProfileForm
from profile_app.models.profile import Profile


def profile_page(req):
    profile = Profile.objects.get()
    expenses = Expense.objects.all()

    profile.budget_left = calculate_left_budget(profile, expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
    }

    return render(req, 'profile.html', context=context)


def profile_edit(req):
    profile = Profile.objects.get()

    if req.method == 'GET':
        form = ProfileForm(instance=profile)

        return visualise_view(req, form, 'profile-edit.html')

    else:
        form = ProfileForm(req.POST,
                           instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

        return visualise_view(req, form, 'profile-edit.html')


def profile_delete(req):
    if req.method == 'GET':
        return render(req, 'profile-delete.html')

    else:
        profile = Profile.objects.get()
        profile.delete()
        [expense.delete() for expense in Expense.objects.all()]
        return redirect('home page')


# Create your views here.
