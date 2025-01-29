from api import views as api_views
from django.urls import path

from userauths import views as userauths_views
from store import views as store_views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("user/token/", userauths_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/', userauths_views.RegisterView.as_view()),
    path('user/password-reset/<email>/', api_views.PasswordResetEmailVerifyAPIView.as_view()),
    path('user/password-change/', api_views.PasswordChangeAPIView.as_view())
]
