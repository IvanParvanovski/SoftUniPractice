from django.shortcuts import render


def index(req):
    return render(req, 'home/landing_page.html')

# Create your views here.
