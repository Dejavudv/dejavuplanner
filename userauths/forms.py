from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import *


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "username"}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={"placeholder": "email"}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "password"}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "comfrim password"}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"full name"}))
    bio = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"bio"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"phone"}))

    class Meta:
        model= Profile
        fields = ["full_name", "image", "bio", "phone"]