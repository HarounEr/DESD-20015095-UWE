from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterFrom#, SignUpForm#, UserUpdateForm, ProfileUpdateForm
#from hello.models import Profile
# Create your views here.
# def update_user_data(user):
#     Profile.objects.update_or_create(user=user, defaults={'club': user.profile.club},)



def register(response):
    if response.method =="POST":
        form = RegisterFrom(response.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            
        return redirect("/login")
    else:
        form = RegisterFrom()
    return render(response, "registerUser/register.html", {"form":form})
