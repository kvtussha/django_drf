from celery import shared_task
from django.core.mail import send_mail

from users.models import Subscription


@shared_task
def send_course_update_notification(course_id):
    # Получите список пользователей, подписанных на обновления данного курса
    subscribed_users = Subscription.objects.filter(course_id=course_id)

    # Отправьте письмо каждому пользователю
    for subscription in subscribed_users:
        subject = 'Обновление материалов курса'
        message = f'Материалы курса {subscription.course.title} были обновлены. Проверьте новые материалы!'
        send_mail(subject, message, 'noreply@gmail.com', [subscription.user.email])
