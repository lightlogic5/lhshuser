from django import forms
from django.utils import timezone

from .models import Employee

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class UserForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'