import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views import View
from markdown.extensions.toc import TocExtension

from blog.models import Post, Category, Tag


def index(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts,
    }
    return render(request, 'blog/index.html', context=context)


def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context=context)


def archive(request, year, month):
    # 调用属性, 使用__, 双下划线
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    print(post_list)
    # post_list = Post.objects.all()
    # for i in post_list:
    #     print(i.created_time, i.created_time.year, i.created_time.month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, cid):
    cate = get_object_or_404(Category, pk=cid)
    post_list = cate.post_set.all()
    # post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, tid):
    tag = get_object_or_404(Tag, pk=tid)
    post_list = tag.post_set.all()
    # post_list = Post.objects.filter(tags=tag).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
