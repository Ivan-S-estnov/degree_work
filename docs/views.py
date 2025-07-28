from rest_framework.permissions import IsAuthenticated, AllowAny
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
from users.permissions import IsModerator, IsOwner


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination
    serializer_class = CourseSerializer


    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == ["create", "update", "retrieve", "list", "destroy"]:
            self.permission_classes = (IsModerator, IsAuthenticated)
        elif self.action in ["retrieve"]:
            self.permission_classes = (~IsModerator | IsOwner)
        return super().get_permissions()

class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator, IsAuthenticated)

class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination
    permission_classes = (IsModerator, IsAuthenticated)


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator, IsAuthenticated)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator | IsOwner, IsAuthenticated)


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator, IsAuthenticated)


class CheckoutCreateAPIView(CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = (IsModerator, IsAuthenticated)


class CheckoutListAPIView(ListAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    pagination_class = CustomPagination
    permission_classes = (IsModerator, IsAuthenticated)


class CheckoutUpdateAPIView(UpdateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = (IsModerator, IsAuthenticated)


class CheckoutRetrieveAPIView(RetrieveAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = (~IsModerator | IsOwner, IsAuthenticated)


class CheckoutDestroyAPIView(DestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = (IsModerator, IsAuthenticated)

