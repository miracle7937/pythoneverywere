from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    email = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'type':"email", 'name':"email" ,'id':"email", 'placeholder':"Your Email"}
    ))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'type':"password", 'name':"pass", 'id':"pass", 'placeholder':"Password"
        }
    ))

    password2 = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'type':"password", 'name':"re_pass",'id':"re_pass", 'placeholder': "Repeat your password"}
    ))

    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'type':"text",'name':"name", 'id':"name", 'placeholder':"Your Name",}
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
