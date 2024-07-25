from django.urls import path, re_path, include
from users.views import dashboard, update_user, manage_users, add_user

urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    path("accounts/update_user/<str:username>", update_user, name="update user"),
    path("accounts/update_user", update_user, name="update user"),
    path("accounts/manage_users/<str:username>", manage_users, name='user_detail'),
    path("accounts/manage_users", manage_users, name = "manage_users"),
    path("accounts/add_user", add_user, name="add_user")

]