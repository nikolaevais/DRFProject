from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

#from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Сourse, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class СourseSerializer(ModelSerializer):
    class Meta:
        model = Сourse
        fields = "__all__"


class СourseDetailSerializer(ModelSerializer):
    count_of_lessons = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_count_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Сourse
        fields = ("title", "description", "count_of_lessons", "lesson")
