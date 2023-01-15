#from django.models import models

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from hello.models import ClubName

class RegisterFrom(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'password1', 'password2')
        #labels = {'club': 'Club Name'}
    # def save(self, commit=True):
    #     # user = super(RegisterFrom, self).save(commit=False)
    #     # user.club = self.cleaned_data["club"]
    #     if commit:
    #         user.save()
    #     return user

