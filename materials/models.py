from django.db import models

from users.models import NULLABLE


# Create your models here.
class Сourse(models.Model):
    title = models.CharField(max_length=35, verbose_name="Название")
    image = models.ImageField(upload_to="materials/course/image/", verbose_name="Превью", **NULLABLE)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f'{self.title} {self.description}'

class Lesson(models.Model):
    title = models.CharField(max_length=35, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="materials/lesson/image/", verbose_name="Превью", **NULLABLE)
    link_to_video = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)
    course = models.ForeignKey(Сourse, on_delete=models.SET_NULL, verbose_name="Курс", **NULLABLE, related_name="course")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f'{self.title} {self.description}'