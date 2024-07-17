from django.contrib.auth.forms import BaseUserCreationForm
from users.models import User
from django.forms import ModelForm

class update_user_form(ModelForm):
    class Meta():
        model = User
        fields = ("username","email","phone_number")