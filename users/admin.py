from django.contrib import admin

from users.models import User, Payments

admin.site.register(User)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'payment_amount', 'payment_method')
