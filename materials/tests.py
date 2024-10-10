from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="lessontest@mail.ru")
        self.course = Course.objects.create(title="Python", description="Описание курса", owner=self.user)
        self.lesson = Lesson.objects.create(title="Django DRF", description="Описание урока", course=self.course,
                                            owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user, is_active=True)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), self.lesson.title
        )

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "title": "JavaZ",
            "description": "Описание Java"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "JavaZ"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), "JavaZ"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': self.lesson.pk, 'title': self.lesson.title, 'description': self.lesson.description,
             'course': self.course.pk, 'image': None, 'link_to_video': None,
             'owner': self.user.pk}]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="lessontest@mail.ru")
        self.course = Course.objects.create(title="Python", description="Описание курса", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_apiview(self):
        url = reverse("materials:subscribe")
        data = {
            "course": self.course.pk,
            "user": self.user.pk
        }

        response = self.client.post(url, data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'message': 'подписка добавлена'}
        )
