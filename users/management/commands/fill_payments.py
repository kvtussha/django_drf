import json
from django.core.management.base import BaseCommand
from users.models import Payments


class Command(BaseCommand):
    help = 'Creates a JSON file with all objects of Payments model'

    def handle(self, *args, **options):
        payments_data = []
        payments = Payments.objects.all()
        print("Number of payments:", payments.count())
        for payment in payments:
            payment_data = {
                'user': payment.user.id,
                'payment_date': payment.payment_date.isoformat(),
                'paid_course': payment.paid_course.id if payment.paid_course else None,
                'paid_lesson': payment.paid_lesson.id if payment.paid_lesson else None,
                'payment_amount': payment.payment_amount,
                'payment_method': payment.payment_method,
            }
            payments_data.append(payment_data)

        with open('payments_all.json', 'w', encoding='utf-8') as f:
            json.dump(payments_data, f, indent=4, ensure_ascii=False)
