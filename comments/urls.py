from django.urls import path

from comments.views import CommentView

app_name = 'comments'
urlpatterns = [
    path('<int:pid>/', CommentView.as_view(), name='comment')
]
