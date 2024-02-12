from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.auth2.invites.views import InvitesView
from src.auth2.signup.views import confirm, signup

invites_router = SimpleRouter()
invites_router.register("invites", InvitesView)


urlpatterns = [
    path("auth2/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth2/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth2/signup/", signup, name="signup-by-email"),
    path("auth2/signup/confirm/<nonce>", confirm, name="signup-confirm"),
]
urlpatterns.extend(invites_router.urls)
