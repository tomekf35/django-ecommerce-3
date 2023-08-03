from django.shortcuts import render


def homepage_view(request):
    section = "homepage"
    return render(request, "core/home.html", {"section": section})


def about_view(request):
    section = "about"
    return render(request, "core/about.html", {"section": section})


def contact_view(request):
    section = "contact"
    return render(request, "core/contact.html", {"section": section})
