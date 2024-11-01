from django.contrib import admin
from materials.models import Course, Lesson, Subscription


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ("title", "description", "course")


@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = ("course", "user", "is_active")
