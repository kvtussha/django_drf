from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=35, verbose_name='phone number', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='country', null=True, blank=True)
    is_password_reset = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=8)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):
    CASH = 'Наличные'
    TRANSFER = 'Перевод на счет'

    METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE,
                                    verbose_name='Оплаченный курс', null=True, blank=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                                    verbose_name='Оплаченный урок', null=True, blank=True)
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=30, choices=METHOD_CHOICES, verbose_name='Метод оплаты')

