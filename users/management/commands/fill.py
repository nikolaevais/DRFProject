from django.core.management import BaseCommand
from users.models import Payment, User
from materials.models import Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_list = [
            {'client': User.objects.get(pk=2), 'date_payment': '2024-08-06', 'payment_course': Course.objects.get(pk=4),
             'payment_amount': '5000', 'method_payment': 'CASH'},
            {'client': User.objects.get(pk=3), 'date_payment': '2024-08-07', 'payment_course': Course.objects.get(pk=3),
             'payment_amount': '1000', 'method_payment': 'CASH'},
            {'client': User.objects.get(pk=4), 'date_payment': '2024-08-07', 'payment_lesson': Lesson.objects.get(pk=3),
             'payment_amount': '500', 'method_payment': 'TRANSFER'},
            {'client': User.objects.get(pk=5), 'date_payment': '2024-08-08', 'payment_course': Course.objects.get(pk=4),
             'payment_amount': '3000', 'method_payment': 'TRANSFER'},
            {'client': User.objects.get(pk=6), 'date_payment': '2024-08-09', 'payment_course': Course.objects.get(pk=3),
             'payment_amount': '4000', 'method_payment': 'CASH'},
            {'client': User.objects.get(pk=7), 'date_payment': '2024-08-09', 'payment_lesson': Lesson.objects.get(pk=5),
             'payment_amount': '600', 'method_payment': 'CASH'},
            {'client': User.objects.get(pk=2), 'date_payment': '2024-08-09', 'payment_course': Course.objects.get(pk=2),
             'payment_amount': '7000', 'method_payment': 'TRANSFER'},
            {'client': User.objects.get(pk=3), 'date_payment': '2024-08-10', 'payment_course': Course.objects.get(pk=2),
             'payment_amount': '8000', 'method_payment': 'TRANSFER'},
            {'client': User.objects.get(pk=4), 'date_payment': '2024-08-10', 'payment_lesson': Lesson.objects.get(pk=7),
             'payment_amount': '800', 'method_payment': 'CASH'},
            {'client': User.objects.get(pk=5), 'date_payment': '2024-08-05', 'payment_course': Course.objects.get(pk=2),
             'payment_amount': '9000', 'method_payment': 'TRANSFER'},

        ]

        payment_for_create = []
        for payment in payment_list:
            payment_for_create.append(
                Payment(**payment)
            )

        Payment.objects.bulk_create(payment_for_create)
