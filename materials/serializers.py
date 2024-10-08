from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import YoutubeValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YoutubeValidator(field="link_to_video")]


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_of_lessons = SerializerMethodField()
    subscription_active = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription_active(self, obj):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=obj).exists()

    class Meta:
        model = Course
        fields = ("id", "title", "description", "count_of_lessons", "lessons", "subscription_active")


class CourseDetailSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"



