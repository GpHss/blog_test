import markdown
from django.db import models
from django.shortcuts import reverse
from django.utils.html import strip_tags


class Category(models.Model):
    name = models.CharField('分类名', max_length=255)

    class Meta:
        verbose_name_plural = verbose_name = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签名', max_length=255)

    class Meta:
        verbose_name_plural = verbose_name = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('标题', max_length=255)
    body = models.TextField('内容')

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    excerpt = models.CharField('摘要', max_length=255, blank=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='分类')

    # 多对多关系会新建一张表, 每一行会存储对应的两个数据间的关系
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')

    class Meta:
        # 后端字段名
        verbose_name_plural = verbose_name = '文章'
        # 自定义排序规则
        ordering = ['-created_time', ]

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url() 方法
    # 返回该文章对应的url链接
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        if self.excerpt == '':
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
            # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])

            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:128] + '...'

        super().save(*args, **kwargs)
