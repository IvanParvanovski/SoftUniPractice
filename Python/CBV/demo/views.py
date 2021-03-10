from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView

from demo.models import Pet


class IndexView(View):
    def get(self, req):
        context = {
            'heading': 'Hello from View!'
        }
        return render(req, 'index.html', context=context)

    def post(self):
        pass


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Hello from TemplateView!'
        context['pets'] = Pet.objects.all()

        return context


class PetListView(ListView):
    template_name = 'index.html'
    model = Pet
    context_object_name = 'pets'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'This is ListView!'

        return context


class PetDetails(DetailView):
    model = Pet
    template_name = 'details.html'

