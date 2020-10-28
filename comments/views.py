from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from blog.models import Post
from comments.forms import CommentForm


class CommentView(View):
    def post(self, request, pid):
        post = get_object_or_404(Post, id=pid)

        form = CommentForm(request.POST)
        if form.is_valid():
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，
            # 但还不保存评论数据到数据库。
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post

            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()
            messages.add_message(request, messages.SUCCESS, '评论发表成功！', extra_tags='success')
            # 重定向到 post 的详情页，
            # 实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)

        # 检查到数据不合法，我们渲染一个预览页面，用于展示表单的错误。
        # 注意这里被评论的文章 post 也传给了模板，因为我们需要根据 post 来生成表单的提交地址。
        context = {
            'post': post,
            'form': form,
        }
        messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
        return render(request, 'comments/preview.html', context=context)
