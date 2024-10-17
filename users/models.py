from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    city = models.CharField(max_length=50, verbose_name="Город", **NULLABLE)
    avatar = models.ImageField(upload_to="users/avatar/", verbose_name="Аватар", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    AMOUNT_PAYMENT = [
        ('CASH', 'Наличные'),
        ('TRANSFER', 'Перевод на счет'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE,
                               related_name="client")
    date_payment = models.DateField(verbose_name='Дата оплаты')
    payment_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Оплаченный курс", **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name="Оплаченный урок", **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    method_payment = models.CharField(max_length=25, verbose_name="Способ оплаты", choices=AMOUNT_PAYMENT)

    session_id = models.CharField(max_length=255, verbose_name="ID сессии", **NULLABLE)
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату", **NULLABLE)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f'{self.date_payment} {self.payment_course if self.payment_course else self.payment_lesson}'
