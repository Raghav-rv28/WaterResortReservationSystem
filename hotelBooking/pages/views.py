from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "website/index.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "website/contact.html", {})


def services_view(request, *args, **kwargs):
    return render(request, "website/services.html", {})


def hotel_view(request, *args, **kwargs):
    return render(request, "website/hotel.html", {})


def blog_view(request, *args, **kwargs):
    return render(request, "website/blog.html", {})
