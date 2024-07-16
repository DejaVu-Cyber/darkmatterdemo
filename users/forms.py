from django.contrib.auth.forms import BaseUserCreationForm
from users.models import User

class CustomUserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = BaseUserCreationForm.Meta.fields + ("email","phone_number",)