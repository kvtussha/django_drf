from rest_framework import viewsets, generics
from rest_framework.generics import DestroyAPIView

from materials.models import Course, Lesson
from materials.paginators import MaterialsPaginator
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.models import Subscription
from materials.tasks import send_course_update_notification


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPaginator


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MaterialsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        # Вызываем задачу Celery для отправки уведомлений об обновлении курса
        send_course_update_notification.delay(instance.id)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionDestroyAPIView(DestroyAPIView):
    queryset = Subscription.objects.all()
