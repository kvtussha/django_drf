from django.contrib import admin

from users.models import User, Payments, Subscription

admin.site.register(User)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'payment_amount', 'payment_method')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'is_subscribed')
