from django.shortcuts import render
from django import views

from blog.models import Category, Post


def index(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
    }
    return render(request, 'wiki/index.html', context=context)


class WikiDetailView(views.View):
    def get(self, requests, cid):
        """显示某个知识库的全部文章"""
        posts = Post.objects.filter(category=cid).order_by('id')
        context = {
            'posts': posts,
        }
        return render(requests, 'wiki/detail.html', context)
