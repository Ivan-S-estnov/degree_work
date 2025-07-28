from rest_framework.serializers import ModelSerializer
from docs.models import Course, Lesson, Checkout
from rest_framework import serializers

from docs.validators import validate_forbidden_words


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ["name", "description", "course", "owner"]


class CheckoutSerializer(ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    right_answer = serializers.CharField(validators=[validate_forbidden_words])


    class Meta:
        model = Checkout
        fields = ["lesson", "question", "answer_first", "answer_second", "answer_third", "right_answer"]