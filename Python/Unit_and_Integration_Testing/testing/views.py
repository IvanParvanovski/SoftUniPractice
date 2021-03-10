
from django.shortcuts import render, redirect

from testing.forms.profile import ProfileForm
from testing.models import Profile


def index(req):
    if req.method == 'GET':
        profiles = Profile.objects.all()
        form = ProfileForm()
        context = {
            'form': form,
            'profiles': profiles
        }

        return render(req, 'index.html', context=context)

    form = ProfileForm(req.POST)

    if form.is_valid():
        form.save()
        return redirect('profiles')

    profiles = Profile.objects.all()

    context = {
        'form': form,
        'profiles': profiles
    }

    return render(req, 'index.html', context=context)

# Create your views here.
