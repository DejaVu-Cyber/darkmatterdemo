from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from users.forms import update_user_form,admin_update_user_form, add_user_form
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from .models import User
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
import string
import secrets
alphabet = string.ascii_letters + string.digits
from django.core.mail import send_mail




@login_required(login_url="accounts/login")
def dashboard(request):
    if request.user is AnonymousUser:
        return render(request, "registration/login.html")
    else:
        return render(request, "users/dashboard.html")
# Create your views here.
@login_required()
def update_user(request, username=None):
    if request.method == "GET" and username is not None:
        return render(
            request, "users/update_user.html",
            {"form": admin_update_user_form(instance=User.objects.get(username=username)), "errors" : None}
        )
    elif request.method == "GET":
        return render(
            request, "users/update_user.html",
            {"form": update_user_form(instance=request.user), "errors": None}
        )
    elif request.method == "POST" and username is not None:
        form = admin_update_user_form(request.POST, instance=User.objects.get(username=username) )
        if form.is_valid():
            user = form.save(commit=False)
            print(type(user))
            if "password" in form.changed_data:
                user.password = make_password(user.password)
            user.save()
            return redirect(reverse("manage_users"))
        else:
            return render(
                request, "users/update_user.html", {"form" : form, "errors" : form.errors}
            )
    elif request.method == "POST":
        form = update_user_form(request.POST,instance=request.user)
        if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect(reverse("manage_users"))
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

def add_user(request):
    if request.method == "GET":
        temp_username = ''.join(secrets.choice(alphabet) for i in range(8))
        data = {
            "username":temp_username
        }
        form = add_user_form(initial=data)
        return render(request,'users/add_user.html',{"form":form})
    if request.method == "POST":
        form = add_user_form(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("activate_user"):
                context = {
                    "username" : form.cleaned_data.get("username"),
                    "password" : form.cleaned_data.get("password1")
                }
                rendered = render_to_string("users/activate_user_email.html",context=context)
                send_mail(subject="activating your darkmatter account",
                          message="",
                          recipient_list=[form.cleaned_data.get("email")],
                          from_email=None, #defaults to whatever is set in settings.py
                          html_message=rendered
                          )
            form.save()
            return render(request,"users/manage_users.html", context = {"user_list": User.objects.all()})




