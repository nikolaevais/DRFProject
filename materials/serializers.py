from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Сourse, Lesson


class СourseSerializer(ModelSerializer):
    class Meta:
        model = Сourse
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_of_lessons = SerializerMethodField()

    def get_count_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()


    class Meta:
        model = Сourse
        fields = ("title", "description", "count_of_lessons")


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"

