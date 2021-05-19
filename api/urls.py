# from allauth.account.views import ConfirmEmailView
# from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path, include
# from django.views.generic import TemplateView

from . import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('', views.ArticleCreateListView.as_view()),
    path('<int:pk>', views.ArticleDetailView.as_view()),
    path('users', views.UserListView.as_view()),
    # path('users/create', views.UserCreateView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
    # path('users/revoke_token', views.RevokeToken.as_view()),
    # path('rest-auth/', include('dj_rest_auth.urls')),
    # path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
