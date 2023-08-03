from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("about", views.about_view, name="about"),
    path("contact", views.contact_view, name="contact"),
]
