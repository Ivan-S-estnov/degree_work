from rest_framework.serializers import ModelSerializer
from docs.models import Course, Lesson, Checkout


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CheckoutSerializer(ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
