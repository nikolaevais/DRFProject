from django.contrib import admin
from users.models import User, Payment

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ("email", "phone")




@admin.register(Payment)
class User(admin.ModelAdmin):
    list_display = ("client", "date_payment", "payment_amount", "method_payment")