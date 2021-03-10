from django.shortcuts import render

from test_app.forms import FormTestCreateForm


def index(req):
    form = FormTestCreateForm()
    context = {
        'form': form,
    }

    return render(req, 'index.html', context=context)

# Create your views here.
