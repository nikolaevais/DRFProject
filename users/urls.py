from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from rest_framework.permissions import AllowAny

from users.views import PaymentListAPIView, UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
        path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
        path("", UserListAPIView.as_view(), name="user_list"),
        path("register/", UserCreateAPIView.as_view(), name="register"),
        path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
        path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
        path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
        path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
        path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
]




