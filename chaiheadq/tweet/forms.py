from django.contrib.auth.models import User
from django import forms
# pyrefly: ignore [missing-import]
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')