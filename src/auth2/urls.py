from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.auth2.invites.views import InvitesView
from src.auth2.signup.views import (
    confirm,
    confirm_change_password,
    init_change_password,
    signup,
)

invites_router = SimpleRouter()
invites_router.register("invites", InvitesView)


urlpatterns = [
    path("auth2/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth2/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth2/signup/", signup, name="signup-by-email"),
    path("auth2/signup/confirm/<nonce>", confirm, name="signup-confirm"),
    path(
        "auth2/signup/password/init-change",
        init_change_password,
        name="init-change-password",
    ),
    path(
        "auth2/signup/password/confirm-change",
        confirm_change_password,
        name="confirm-change-password",
    ),
]
urlpatterns.extend(invites_router.urls)
