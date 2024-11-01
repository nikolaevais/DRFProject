from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from datetime import timedelta
from django.utils import timezone

from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_course_update_email(course_id):
    """ Отправляет сообщение пользователю об обновлении """
    course = Course.objects.get(pk=course_id)
    course_sub = Subscription.objects.filter(course=course_id)
    for sub in course_sub:
        send_mail(subject=f"Обновление {course.title}",
                  message=f"Курс {course.title} был обновлен",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[f'{sub.user}'],
                  fail_silently=True
                  )


@shared_task
def check_inactive_users():
    """Функция проверки активности пользователя"""
    users = User.objects.filter(is_active=True, is_staff=False, is_superuser=False, last_login__isnull=False)
    date_delta = timedelta(1)
    for user in users:
        date_block = timezone.now() - date_delta
        if user.last_login < date_block:
            print('Блокировка пользователя')
            user.is_active = False
            user.save()

