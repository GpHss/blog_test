from django.shortcuts import render
from django.views import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('这是wiki主页')