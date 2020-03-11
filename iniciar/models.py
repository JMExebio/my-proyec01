from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({
            'class': 'form-control'
        }))
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput({
            'class': 'form-control'
        }))
