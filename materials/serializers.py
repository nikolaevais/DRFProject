from rest_framework.serializers import ModelSerializer

from materials.models import Сourse, Lesson


class СourseSerializer(ModelSerializer):
    class Meta:
        model = Сourse
        fields = "__all__"


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"

