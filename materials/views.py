import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson, Subscription
from materials.paginations import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, SubscriptionSerializer
from materials.tasks import send_course_update_email
from users.permissions import IsModerator, IsOwmer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator)
        elif self.action == ['retrieve', 'update']:
            self.permission_classes = (IsModerator | IsOwmer,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModerator | IsOwmer,)
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        updated_course = serializer.save()
        if updated_course:
            send_course_update_email.delay(updated_course.id)


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwmer)


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwmer)


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwmer | ~IsModerator)


class SubscriptionAPIView(APIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, IsOwmer | IsModerator)

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subscription, created = Subscription.objects.get_or_create(user=user, course=course_item)

        if created:
            message = 'подписка добавлена'
        else:
            subscription.delete()
            message = 'подписка удалена'
        # Возвращаем ответ в API
        return Response({"message": message})
