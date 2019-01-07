from django.shortcuts import render, get_object_or_404
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from authenticate.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password1 = forms.CharField(
        label='password1', max_length=100, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    # password3 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password4 = forms.CharField(
    #     label='Password confirmation', widget=forms.PasswordInput)
    # text = forms.TextInput()
    # email = forms.EmailField(label='email', unique=True)
    # username = forms.CharField(label='username', unique=True)

    class Meta:
        model = MyUser
        fields = ['email', 'username']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
