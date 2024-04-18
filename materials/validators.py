from rest_framework_simplejwt import serializers


class LessonVideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_link = dict(value).get(self.field)
        if not video_link.startswith('https://www.youtube.com/'):
            message = 'Ссылка не поддерживается'
            raise serializers.ValidationError(message)
