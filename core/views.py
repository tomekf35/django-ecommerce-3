from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm


def homepage_view(request):
    section = "homepage"
    return render(request, "core/home.html", {"section": section})


def about_view(request):
    section = "about"
    return render(request, "core/about.html", {"section": section})


def contact_view(request):
    section = "contact"
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email_from = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            subject = f"Bookstore message from {name}"
            try:
                send_mail(subject, message, email_from, ["admin@bookstore.com"])
                messages.success(request, "Message has been sent!")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("core:contact")
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"section": section})
