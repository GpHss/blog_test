from django.contrib import admin

from blog.models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'modified_time', 'created_time', ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
