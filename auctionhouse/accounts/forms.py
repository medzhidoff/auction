from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Profile
from django.forms.widgets import DateInput

# create a new class that inherits from suer creation form
class UserLoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'bg-teal-10 border border-coolGray-300 rounded-sm w-full text-coolGray-600 placeholder-coolGray-400 transition duration-500 focus:shadow-lg focus:border-teal-400 focus:outline-none px-4 py-3.5'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'bg-teal-10 border border-coolGray-300 rounded-sm w-full text-coolGray-600 placeholder-coolGray-400 transition duration-500 focus:shadow-lg focus:border-teal-400 focus:outline-none px-4 py-3.5'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'dob', 'name', 'surname', 'patronymic']
        labels = {
            'dob': ('Date of birth'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }