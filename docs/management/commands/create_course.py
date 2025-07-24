from django.core.management import BaseCommand

from docs.models import Course, Lesson

class Command(BaseCommand):

    def handle(self, *args, **option):
        """ Create course and lesson"""

        course1, _ = Course.objects.get_or_create(name="Django REST framework",
                       description="Библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта")

        lesson =[
            {
            "name": "Сериализаторы",
            "description": "Сериализаторы в DRF представляют собой класс, используемый для преобразования сложных типов данных, таких как модели Django, в форматы, пригодные для передачи по сети, например JSON",
            "course": course1
            },
            {
            "name": "Вложенные данные",
            "description": "Это расширяемые поля, в которые можно вкладывать результат работы других сериализаторов",
            "course": course1
            }
        ]

        for lesson_data in lesson:
            lesson, created = Lesson.objects.get_or_create(**lesson_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully added product: {lesson.name}'))
        else:
            self.stdout.write(self.style.WARNING(f'Product already exist: {lesson.name}'))

