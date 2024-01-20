from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.auth.signup.views import confirm, signup

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", signup, name="signup-by-email"),
    path("signup/confirm/", confirm, name="signup-confirm"),
]
