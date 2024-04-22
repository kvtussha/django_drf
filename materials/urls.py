from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
      LessonUpdateAPIView, LessonDestroyAPIView, CourseCreateAPIView, SubscriptionCreateAPIView, \
      SubscriptionUpdateAPIView, SubscriptionDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
      path('create/', CourseCreateAPIView.as_view(), name='course-create'),

      path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
      path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
      path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-get'),
      path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson-update'),
      path('lesson/destroy/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-destroy'),

      path('subscription/create', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
      path('subscription/update/<int:pk>', SubscriptionUpdateAPIView.as_view(), name='subscription-update'),
      path('subscription/destroy/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='subscription-destroy'),
 ] + router.urls
