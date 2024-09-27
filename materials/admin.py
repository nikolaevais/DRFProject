from django.contrib import admin
from materials.models import Course, Lesson


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ("title", "description", "course")
