from os.path import join, isfile

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView

from python_core.decorators import group_required
from templates_advanced_app.forms import PythonCreateForm, FilterForm
from templates_advanced_app.models import Python


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''
    return {
        'text': text,
        'order': order
    }
#
#
# @login_required
# def index(req):
#     params = extract_filter_values(req.GET)
#     order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
#
#     pythons = Python.objects.filter(name__icontains=params['text']).order_by(order_by)
#     for python in pythons:
#         print(req.user)
#         python.can_delete = python.created_by == req.user
#
#     context = {
#         'pythons': pythons,
#         'filter_form': FilterForm(initial=params)
#     }
#     return render(req, 'index.html', context=context)


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    ordered_by_asc = True

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        self.ordered_by_asc = params['order'] == FilterForm.ORDER_ASC
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pythons'] = sorted(context['pythons'], key=lambda x: x.name, reverse=not self.ordered_by_asc)
        context['filter_form'] = FilterForm(initial={'order': self.ordered_by_asc})
        return context


# @login_required(login_url='login user')
# # @group_required(groups=['Regular User'])
# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#
#         context = {
#             'form': form
#         }
#
#         return render(req, 'create.html', context=context)
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         context = {
#             'form': form
#         }
#
#         return render(req, 'create.html', context=context)


# @method_decorator(group_required(groups=['Regular User']), name='dispatch')
class PythonCreateView(LoginRequiredMixin, FormView):
    form_class = PythonCreateForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def server_private_file(req, path_to_file):
    full_path = join(settings.MEDIA_ROOT, 'private', path_to_file)
    if isfile(full_path):
        has_access = True
        if has_access:
            file = open(full_path, 'rb')
            response = HttpResponse(content=file)
            response['Content-Disposition'] = 'attachment'
            return response
    return None
