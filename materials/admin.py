from django.contrib import admin
from materials.models import Сourse, Lesson


@admin.register(Сourse)
class Course(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ("title", "description", "course")
