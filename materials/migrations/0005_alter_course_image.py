# Generated by Django 5.0.4 on 2024-04-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='undefined', null=True, upload_to='course/', verbose_name='Изображение'),
        ),
    ]