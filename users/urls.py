from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserCreateApiView

app_name = UsersConfig.name

urlpatterns = [
    path('check/', UserCreateApiView.as_view(), name='register'),
    path('talk/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('new/', TokenRefreshView.as_view(), name='token_refresh'),

]