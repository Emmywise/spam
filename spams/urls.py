from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from spams.views import (
    SignUp, UserContact, SearchNumber, SearchName, Spams
)

urlpatterns = [
    path("sign-up", SignUp.as_view(), name="sign_up"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("contact", UserContact.as_view(), name="contact"),
    path("search-number", SearchNumber.as_view(), name="search_name"), 
    path("search-name", SearchName.as_view(), name="search_number"),
    path("spam", Spams.as_view(), name="spam"), 
]