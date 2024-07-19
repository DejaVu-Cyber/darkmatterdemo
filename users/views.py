from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from users.forms import update_user_form,admin_update_user_form
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from .models import User
from django.contrib.auth.hashers import make_password



@login_required(login_url="accounts/login")
def dashboard(request):
    if request.user is AnonymousUser:
        return render(request, "registration/login.html")
    else:
        return render(request, "users/dashboard.html")
# Create your views here.
@login_required()
def update_user(request, username=None):
    user = None
    form = None
    if username is None:
        user = request.user
        form = update_user_form(instance=user)
    else:
        user = User.objects.get(username=username)
        form = admin_update_user_form(instance=user)
    if request.method == "GET" :
        return render(
            request, "users/update_user.html",
            {"form": form, "errors" : None}
        )
    elif request.method == "POST":
        if username is None:
            form = update_user_form(request.POST, instance=user)
        else:
            form = admin_update_user_form(request.POST, instance=user)
        if form.is_valid():

            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return render(
                request, "users/update_user.html", {"form" : form, "errors" : form.errors}
            )
def manage_users(request,username=None):

    if request.method == "GET" and username is not None:
        return render(request,"users/user_detail.html",{"user_list":User.objects.all(),"current_user":User.objects.get(username=username)})
    elif request.method == "GET":
        return render(request, "users/manage_users.html",
                      {"user_list": User.objects.all()})

