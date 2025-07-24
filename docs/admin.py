from django.contrib import admin

from docs.models import Course, Lesson, Checkout


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "owner")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "course", "owner")

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ("lesson", "question", "answer_first", "answer_second", "answer_third", "right_answer")