# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, './lobby/index.html')

#
# def index(req):
#     return HttpResponse('<u>Hi!</u>')
