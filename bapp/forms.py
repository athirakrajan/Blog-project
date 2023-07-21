from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class UserAddForm(UserCreationForm):
    class meta:
        Model=User
        files=["username","email","password1","password2"]