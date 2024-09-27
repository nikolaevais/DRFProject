from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("title", "description", "count_of_lessons", "lessons")


class CourseDetailSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"
