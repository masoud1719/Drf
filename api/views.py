from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

class ArticleCreateListView(ListCreateAPIView):
    queryset = Article.objects.all()
    model = Article
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserCreateListView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
