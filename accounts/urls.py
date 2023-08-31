from django.urls import path
from allauth.account.views import confirm_email
from . import views


urlpatterns = [
    path(
        "accounts/confirm-email/<str:key>/", confirm_email, name="account_confirm_email"
    ),
    path("profile/<str:username>/", views.user_profile_view, name="user_profile"),
    path(
        "profile/<str:username>/purchases",
        views.user_purchases_view,
        name="user_purchases",
    ),
]
