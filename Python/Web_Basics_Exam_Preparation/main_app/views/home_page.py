from django.shortcuts import render, redirect

from main_app.common.budget import calculate_left_budget
from main_app.models.expense import Expense
from main_app.views.shared import visualise_view
from profile_app.forms.profile import ProfileForm
from profile_app.models.profile import Profile


def home_page(req):
    profiles = Profile.objects.all()

    if profiles:
        user_profile = Profile.objects.get()
        expenses = Expense.objects.all()
        user_profile.budget_left = calculate_left_budget(user_profile, expenses)

        context = {
            'profile': user_profile,
            'expenses': expenses,
        }

        return render(req, 'home-with-profile.html', context=context)

    else:
        if req.method == 'GET':
            form = ProfileForm()
            return visualise_view(req, form, 'home-no-profile.html')

        else:
            form = ProfileForm(req.POST)

            if form.is_valid():
                form.save()
                return redirect('home page')

            return visualise_view(req, form, 'home-no-profile.html')
