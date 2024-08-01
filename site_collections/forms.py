from django import forms
from django.forms import ModelForm
from .models import collection_target
class chat_form(forms.Form):
    question = forms.CharField(label="question", max_length=500)
class collection_target_form(ModelForm):
    class Meta:
        model = collection_target
        fields = ["name","type","language","host_url"]