from django.contrib.auth.forms import BaseUserCreationForm
from users.models import User
from django.forms import ModelForm
from django import forms
import string
import secrets
alphabet = string.ascii_letters + string.digits

class update_user_form(ModelForm):
    class Meta():
        model = User
        fields = ("username","email","phone_number")
class admin_update_user_form(ModelForm):

    class Meta():
        model = User
        fields = ("username","email","phone_number","password","collection_manager","is_superuser")

class add_user_form(BaseUserCreationForm):
    activate_user = forms.BooleanField(widget=forms.CheckboxInput())
    class Meta:
        model = User
        fields = ("username","password1","password2","email")

    def __init__(self, *args, **kwargs):
        super(BaseUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
    def clean_password2(self):
        if self.cleaned_data.get("password1") == "":
            self.cleaned_data["password1"] = ''.join(secrets.choice(alphabet) for i in range(8))
            self.cleaned_data["password2"] = self.cleaned_data["password1"]
        return self.cleaned_data.get("password2")
