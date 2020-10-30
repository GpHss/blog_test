from django.urls import path

from wiki.views import index, WikiDetailView

app_name = 'wiki'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:cid>/', WikiDetailView.as_view(), name='detail'),
]