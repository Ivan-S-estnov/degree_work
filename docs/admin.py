from django.contrib import admin

from docs.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course', 'owner')
