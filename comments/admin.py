from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'email', 'url', 'post', 'created_time']


admin.site.register(Comment, CommentAdmin)
