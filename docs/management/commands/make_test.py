from django.core.management import BaseCommand

from docs.models import Lesson, Checkout

class Command(BaseCommand):

    def handle(self, *args, **option):
        """ Create course and lesson"""

        lesson1, _ = Lesson.objects.get_or_create(name="Django REST framework",
                       description="Библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта")