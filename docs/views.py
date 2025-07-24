from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from docs.models import Course, Lesson, Checkout
from docs.paginators import CustomPagination
from docs.serializers import CourseSerializer, LessonSerializer, CheckoutSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination
    serializer_class = CourseSerializer


    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CheckoutCreateAPIView(CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CheckoutListAPIView(ListAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    pagination_class = CustomPagination


class CheckoutUpdateAPIView(UpdateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CheckoutRetrieveAPIView(RetrieveAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class CheckoutDestroyAPIView(DestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
