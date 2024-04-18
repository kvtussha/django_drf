from django.urls import reverse_lazy
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
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        url = reverse_lazy('materials:lesson-create')
        data = {'title': 'New Lesson', 'course': self.course.id,
                'video': 'https://www.youtube.com/', 'description': '-'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        # Проверяем получение информации об уроке
        url = f'/lesson/{self.lesson1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, LessonSerializer(self.lesson1).data)

    def test_update_lesson(self):
        # Проверяем обновление информации об уроке
        url = f'lesson/update/{self.lesson1.id}/'
        data = {'title': 'Updated Lesson'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Lesson')

    def test_delete_lesson(self):
        # Проверяем удаление урока
        url = f'/lesson/destroy/{self.lesson1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Создаем тестовый курс
        self.course = Course.objects.create(title='Test Course')

        # Создаем клиент API и аутентифицируемся как тестовый пользователь
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        # Проверяем подписку на курс
        url = '/materials/subscription/'
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), True)

    def test_unsubscribe_from_course(self):
        # Подписываемся на курс
        url = '/materials/subscription/'
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), False)
