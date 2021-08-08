from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from dashboard import models
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class UserUpdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username']

class UserProfileform(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['about', 'phone', 'address','photo']     

class PassChange(PasswordChangeForm):
    class Meta:
        model  = User
        fields = "__all__"

class AreaForm(forms.ModelForm):
    class Meta:
        model = models.Areas
        fields = "__all__"