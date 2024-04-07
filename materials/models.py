from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса')
    image = models.ImageField(upload_to='course/', verbose_name='Изображение')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название урока')
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    video = models.TextField(verbose_name='Видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
