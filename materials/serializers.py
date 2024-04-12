from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'image', 'description', 'video')


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    all_lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_lessons_count(instance):
        return instance.lesson_set.count()
