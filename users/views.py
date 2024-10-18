from rest_framework import filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.serializers import PaymentSerializer, UserSerializer
from users.models import Payment, User
from users.services import create_stripe_price, create_stripe_session, create_stripe_product


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [filters.OrderingFilter]
    filterset_fields = ('payment_course', 'payment_lesson', 'method_payment')
    ordering_fields = ['date_payment']


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(client=self.request.user)
        product = create_stripe_product(payment)
        price = create_stripe_price(product, payment.payment_amount)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get('password'))
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
