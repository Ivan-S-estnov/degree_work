from django.urls import path
from rest_framework.routers import SimpleRouter
from docs.apps import DocsConfig
from docs.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
    CheckoutListAPIView,
    CheckoutRetrieveAPIView,
    CheckoutCreateAPIView,
    CheckoutUpdateAPIView,
    CheckoutDestroyAPIView
)

app_name = DocsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)
urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="retrieve"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="create"),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="update"),
    path("lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="destroy"),
    path("test/", CheckoutListAPIView.as_view(), name="test_list"),
    path("test/<int:pk>/", CheckoutRetrieveAPIView.as_view(), name="test_retrieve"),
    path("test/create/", CheckoutCreateAPIView.as_view(), name="create_test"),
    path("test/<int:pk>/update/", CheckoutUpdateAPIView.as_view(), name="update_test"),
    path(
        "test/<int:pk>/delete/", CheckoutDestroyAPIView.as_view(), name="destroy_test"
    ),
]
urlpatterns += router.urls
