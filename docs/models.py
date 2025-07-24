from django.conf import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите владельца курса",
    )
    # link = models.URLField(verbose_name="url-курса", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", blank=True, null=True)
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="lessons",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите владельца урока",
    )
    # link = models.URLField(verbose_name="url-урока", blank=True, null=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class Checkout(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Материал теста",
        related_name="lessons",
    )
    question = models.TextField(verbose_name="Вопрос")
    answer_first = models.CharField(max_length=200, verbose_name="Ответ_1", null=False)
    answer_second = models.CharField(max_length=200, verbose_name="Ответ_2", null=False)
    answer_third = models.CharField(max_length=200, verbose_name="Ответ_3", null=True)
    right_answer = models.CharField(
        max_length=200, verbose_name="Правильный ответ", null=False
    )

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.question
