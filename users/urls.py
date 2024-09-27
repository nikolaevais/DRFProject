from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import PaymentListAPIView, UserListAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
        path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
        path("", UserListAPIView.as_view(), name="user_list")
]

