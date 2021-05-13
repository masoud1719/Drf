from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('<int:pk>', views.ArticleDetail.as_view(), name='article-detail'),
]
