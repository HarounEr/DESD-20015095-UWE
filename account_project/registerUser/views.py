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

            #new data
            user.profile.club = form.changed_data('club')
            #update_user_data(user)

            # load the profile
            user.save()
            

        return redirect("/login")
    else:
        form = RegisterFrom()
    return render(response, "registerUser/register.html", {"form":form})

# def profile(response):
#     if response.method == 'POST':
#         u_form = UserUpdateForm(response.POST, instance=response.user)
#         p_form = ProfileUpdateForm(response.POST, instance=response.user.profile)
        
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             #messages.success(response, f'Your profile has been updated')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=response.user)
#         p_form = ProfileUpdateForm(instance=response.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(response, "registerUser/register.html", {"form":form})