from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Hereda de UserCreationForm par agregar valores
from .models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'address')
