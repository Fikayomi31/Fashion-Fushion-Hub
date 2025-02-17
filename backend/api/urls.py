from api import views as api_views
from django.urls import path

from userauths import views as userauths_views
from store import views as store_views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # User Endpoint
    path("user/token/", userauths_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/', userauths_views.RegisterView.as_view()),
    path('user/password-reset/<email>/', userauths_views.PasswordEmailVerify.as_view()),
    path('user/password-change/', userauths_views.PasswordChangeView.as_view()),

    # Store Endpoint
    path('category/', store_views.CategoryListAPIView.as_view()),
    path('products/', store_views.ProductListAPIView.as_view()),
    path('products/<slug>', store_views.ProductDetailAPIView.as_view()),
    path('cart/', store_views.CartAPIView.as_view())
]

