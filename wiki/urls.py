from django.urls import path

from wiki.views import index

app_name = 'wiki'
urlpatterns = [
    path('', index, name='index'),
]