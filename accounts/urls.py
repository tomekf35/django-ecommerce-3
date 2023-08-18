from django.urls import path
from allauth.account.views import confirm_email

urlpatterns = [
    path(
        "accounts/confirm-email/<str:key>/", confirm_email, name="account_confirm_email"
    ),
]
