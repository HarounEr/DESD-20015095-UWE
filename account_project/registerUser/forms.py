#from django.models import models

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from hello.models import ClubName

class RegisterFrom(UserCreationForm):
    #First_Name = forms.CharField(max_length=50)
    #Last_Name = forms.CharField(max_length=1)
    #club= forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'password1', 'password2')
        #labels = {'club': 'Club Name'}
    def save(self, commit=True):
        user = super(RegisterFrom, self).save(commit=False)
        #user.club = self.cleaned_data["club"]
        if commit:
            user.save()
        return user

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User 
#         fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     city = forms.CharField(label='City', max_length=100)
#     state = forms.CharField(label='State', required=False, max_length=50)
#     country = forms.CharField(label='Country (if outside U.S.)', required=False, max_length=100)
#     favorite_artists = forms.CharField(label='Your favorite artists (use commas)', required=False, max_length=200)
#     about_user = forms.CharField(widget=forms.Textarea(attrs={"rows": 7}), label='A small description of yourself', required=False)

# class Meta:
#         model = ClubName
#         fields = ['city', 'state', 'country', 'favorite_artists', 'about_user']

# class ProfileUpdateForm(forms.ModelForm):
#     city = forms.CharField(label='City', max_length=100)
#     state = forms.CharField(label='State', required=False, max_length=50)
#     country = forms.CharField(label='Country (if outside U.S.)', required=False, max_length=100)
#     favorite_artists = forms.CharField(label='Your favorite artists (use commas)', required=False, max_length=200)
#     about_user = forms.CharField(widget=forms.Textarea(attrs={"rows": 7}), label='A small description of yourself', required=False)

# class Meta:
#         model = ClubName
#         fields = ['city', 'state', 'country', 'favorite_artists', 'about_user']