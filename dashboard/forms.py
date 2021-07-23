from django import forms
from django.contrib.auth.models import User
from dashboard.models import Profile

class UserUpdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username']

class UserProfileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'phone', 'address','photo']     