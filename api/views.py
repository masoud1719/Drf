from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    ListAPIView
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsOwnerOrReadOnly, IsSuperorAnanymouswriteonly


class ArticleCreateListView(ListCreateAPIView):
    queryset = Article.objects.all()
    model = Article
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsStaffOrReadOnly, IsOwnerOrReadOnly]


class UserListView(ListAPIView):
    permission_classes = [IsSuperUser]

    def get_queryset(self):
        print(self.request.user)
        return User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):

    permission_classes = [AllowAny]
    def get_queryset(self):
        print(self.request.user)
        return User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    permission_classes = [IsSuperUser]

    def get_queryset(self):
        print(self.request.user)
        return User.objects.all()
    serializer_class = UserSerializer
