from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Category


def index(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
    }
    return render(request, 'wiki/index.html', context=context)
