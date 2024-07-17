from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from users.forms import update_user_form
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser


@login_required(login_url="accounts/login")
def dashboard(request):
    if request.user is AnonymousUser:
        return render(request, "registration/login.html")
    else:
        return render(request, "users/dashboard.html")
# Create your views here.
@login_required()
def update_user(request):
    if request.method == "GET":
        return render(
            request, "users/update_user.html",
            {"form": update_user_form(instance=request.user), "errors" : None}
        )
    elif request.method == "POST":
        form = update_user_form(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return render(
                request, "users/update_user.html", {"form" : update_user_form(instance=request.user), "errors" : form.errors}
            )