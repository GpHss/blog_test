from django.urls import path

from blog.views import index, detail, archive, category, tag

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', detail, name='detail'),
    path('archives/<int:year>/<int:month>/', archive, name='archive'),
    path('category/<int:cid>/', category, name='category'),
    path('tag/<int:tid>/', tag, name='tag'),

]
