from django.shortcuts import render

from blog.models import Category


def index(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
    }
    return render(request, 'wiki/index.html', context=context)
