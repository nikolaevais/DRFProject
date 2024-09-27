from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import PaymentListAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
        path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
]

