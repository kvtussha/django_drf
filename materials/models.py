from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса', unique=True)
    image = models.ImageField(upload_to='course/', verbose_name='Изображение',
                              null=True, blank=True, default="undefined")
    description = models.CharField(max_length=500, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название урока', unique=True)
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение',
                              null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    video = models.TextField(verbose_name='Видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
