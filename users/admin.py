from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "last_login", "is_active")


@admin.register(Payment)
class User(admin.ModelAdmin):
    list_display = ("client", "date_payment", "payment_amount", "method_payment")