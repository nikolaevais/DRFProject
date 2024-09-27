from rest_framework import filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


from users.serializers import PaymentSerializer
from users.models import Payment


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [filters.OrderingFilter]
    filterset_fields = ('payment_course', 'payment_lesson', 'method_payment')
    ordering_fields = ['date_payment']
