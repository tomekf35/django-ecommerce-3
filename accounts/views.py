from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_profile_view(request, username):
    return render(request, "profile/profile.html")


@login_required
def user_purchases_view(request, username):
    return render(request, "profile/purchases.html")
