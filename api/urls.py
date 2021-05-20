# from allauth.account.views import ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path, include
# from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from . import views
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()

router.register('articles', views.ArticleViewSet),
router.register('users', views.UserViewSet),
urlpatterns = [

    # path('users', views.UserListView.as_view()),
    # path('users/<int:pk>', views.UserDetailView.as_view()),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include(router.urls)),

]
