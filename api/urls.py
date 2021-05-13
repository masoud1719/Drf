from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ArticleCreateListView.as_view()),
    path('<int:pk>', views.ArticleDetailView.as_view()),
    path('users', views.UserCreateListView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
]
