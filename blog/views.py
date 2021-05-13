from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    model = Article
    queryset = Article.objects.filter(status=True)
    context_object_name = 'article_list'


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):
        return get_object_or_404(Article, pk=self.kwargs.get('pk'))
