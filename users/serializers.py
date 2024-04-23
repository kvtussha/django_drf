from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_date', 'paid_course', 'paid_lesson',
                  'payment_amount', 'payment_method')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country',
                  'is_active', 'is_staff')