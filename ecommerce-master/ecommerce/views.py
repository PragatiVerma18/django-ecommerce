from django.contrib.auth import authenticate, login, logout, get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product
from .forms import ContactForm

def home_page(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About page",
        "content":"Welcome to About page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Welcome to Contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)
