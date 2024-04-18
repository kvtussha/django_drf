from rest_framework import serializers
from materials.models import Course, Lesson
from materials.validators import LessonVideoValidator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'image', 'description', 'video')
        validators = [LessonVideoValidator(field='video')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    all_lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_lessons_count(instance):
        return instance.lesson_set.count()

    @staticmethod
    def get_is_subscribed(obj):
        return obj.is_subscribed


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'course', 'is_subscribed']
