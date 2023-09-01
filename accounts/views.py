from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser


@login_required
def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, "profile/profile.html", {"user": user})


@login_required
def user_purchases_view(request, username):
    return render(request, "profile/purchases.html")
