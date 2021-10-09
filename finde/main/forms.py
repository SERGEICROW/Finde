from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Hereda de UserCreationForm par agregar valores
from .models import UserProfile, List


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CurpUpdate(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['curp']


class PhoneUpdate(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone']


class BAddressUpdate(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address']


class CreateList(ModelForm):
    class Meta:
        model: List
        fields = ['title']