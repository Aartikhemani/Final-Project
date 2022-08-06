from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from app.models import Customer


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email = forms.CharField(required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username': forms.TextInput}


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','city','zipcode','state','country']
# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput)
#     password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput)


# class MyPasswordResetForm(PasswordResetForm):
#     email = forms.EmailField(label=_('Email'), max_length=200, widget=forms.EmailInput)