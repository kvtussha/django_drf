import os

import django
from django.conf import settings
from django.urls import reverse, reverse_lazy
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from users.models import User, Subscription
from .models import Course, Lesson
from .serializers import LessonSerializer


class LessonTestCase(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(email='testuser@gmail.com', username='testuser', password='password123')

        # Создаем тестовый курс
        self.course = Course.objects.create(title='Test Course')

        # Создаем тестовые уроки
        self.lesson1 = Lesson.objects.create(title='Lesson 1', course=self.course,
                                             description='-', video='https://www.youtube.com/')
        self.lesson2 = Lesson.objects.create(title='Lesson 2', course=self.course,
                                             description='-', video='https://www.youtube.com/')

        # Создаем клиент API и аутентифицируемся как тестовый пользователь
        self.client = APIClient()
        self.client2 = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        url = reverse_lazy('materials:lesson-create')
        data = {'title': 'New Lesson', 'course': self.course.id,
                'video': 'https://www.youtube.com/', 'description': '-'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        # Проверяем получение информации об уроке
        url = f'/lesson/{self.lesson1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, LessonSerializer(self.lesson1).data)

    def test_update_lesson(self):
        # Проверяем обновление информации об уроке
        url = f'/lesson/update/{self.lesson1.id}'
        data = {'title': 'New Lesson is updated', 'course': self.course.id,
                'video': 'https://www.youtube.com/', 'description': '---'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['title'], 'Updated Lesson')

    def test_delete_lesson(self):
        url = f'/lesson/destroy/{self.lesson2.id}'
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Создаем тестовый курс
        self.course = Course.objects.create(title='Test Course')
        self.course2 = Course.objects.create(title='Test Course 2')

        # Создаем клиент API и аутентифицируемся как тестовый пользователь
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        url = reverse_lazy('materials:subscription-create')
        data = {'course': self.course.id, 'user': self.user.id, 'is_subscribed': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course2, is_subscribed=True)
        url = reverse_lazy('materials:subscription-destroy', args=[subscription.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course2).exists())
