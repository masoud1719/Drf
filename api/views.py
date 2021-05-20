from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    ListAPIView
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsOwnerOrReadOnly, IsSuperorAnanymouswriteonly
from rest_framework.viewsets import ModelViewSet


# class ArticleCreateListView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     model = Article
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsStaffOrReadOnly, IsOwnerOrReadOnly]


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_class = [IsStaffOrReadOnly]
        else:
            permission_class = [IsStaffOrReadOnly, IsOwnerOrReadOnly]
        return [permission() for permission in permission_class]


class UserViewSet(ModelViewSet):
    permission_classes = [IsSuperUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserListView(ListAPIView):
#     permission_classes = [IsSuperUser]
#
#     def get_queryset(self):
#         print(self.request.user)
#         return User.objects.all()
#
#     serializer_class = UserSerializer
#
#
# class UserDetailView(RetrieveAPIView):
#     permission_classes = [IsSuperUser]
#
#     def get_queryset(self):
#         print(self.request.user)
#         return User.objects.all()
#
#     serializer_class = UserSerializer
