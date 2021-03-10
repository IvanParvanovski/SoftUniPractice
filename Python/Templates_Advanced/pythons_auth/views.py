from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from pythons_auth.forms import RegisterForm, ProfileForm, LoginForm


# @transaction.atomic
# def register_user(req):
#     if req.method == 'GET':
#         user_form = RegisterForm()
#         user_profile = ProfileForm()
#         context = {
#             'user_form': user_form,
#             'user_profile': user_profile
#         }
#
#         return render(req, 'auth/register.html', context=context)
#     else:
#         user_form = RegisterForm(req.POST)
#         user_profile = ProfileForm(req.POST, req.FILES)
#
#         if user_form.is_valid() and user_profile.is_valid():
#             user = user_form.save()
#             profile = user_profile.save(commit=False)
#             profile.user = user
#             profile.save()
#             login(req, user)
#             return redirect('index')
#
#         context = {
#             'user_form': user_form,
#             'user_profile': user_profile
#         }
#
#         return render(req, 'auth/register.html', context=context)


# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'auth/register.html'
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = context['form']
#         context['profile_form'] = ProfileForm()
#
#         return context
#
#     def form_valid(self, form):
#         pass


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegisterForm()
        context['profile_form'] = ProfileForm()

        return context

    def post(self, req):
        user_form = RegisterForm(req.POST)
        user_profile = ProfileForm(req.POST, req.FILES)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            profile = user_profile.save(commit=False)
            profile.user = user
            profile.save()
            login(req, user)
            return redirect('index')

        context = {
            'user_form': user_form,
            'user_profile': user_profile
        }

        return render(req, 'auth/register.html', context=context)


def get_redirect_url(params):
    redirect_url = params.get('redirect_url')
    return redirect_url if redirect_url else 'index'


def login_user(req):
    if req.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(req, 'auth/login.html', context)
    else:
        login_form = LoginForm(req.POST)

        return_url = get_redirect_url(req.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(req, user)
                return redirect(return_url)

        context = {
            'login_form': login_form,
        }
        return render(req, 'auth/login.html', context=context)


def logout_user(req):
    logout(req)
    return redirect('index')


# Create your views here.
