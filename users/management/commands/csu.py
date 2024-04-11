import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin2@sky.pro",
            is_staff=True,
            is_superuser=True,
            verification_code='123456',
        )
        user.set_password('admin')
        user.is_active = True
        user.save()
