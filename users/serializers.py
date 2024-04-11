from rest_framework import serializers

from users.models import Payments, User


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('payment_date', 'paid_course', 'paid_lesson',
                  'payment_amount', 'payment_method')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country',
                  'is_active', 'is_staff')