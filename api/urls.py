from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ArticleCreateListView.as_view()),
    path('<int:pk>', views.ArticleDetailView.as_view()),
    path('users', views.UserListView.as_view()),
    path('users/create', views.UserCreateView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
    path('users/revoke_token', views.RevokeToken.as_view()),
]
