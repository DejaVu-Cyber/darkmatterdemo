from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from users.forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser


@login_required
def dashboard(request):
    if request.user is AnonymousUser:
        return render(request, "registration/login.html")
    else:
        return render(request, "users/dashboard.html")
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm, "errors" : None}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("yuh")
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return render(
                request, "users/register.html", {"form" : CustomUserCreationForm, "errors" : form.errors}
            )