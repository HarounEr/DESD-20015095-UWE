from django.shortcuts import render, redirect, get_object_or_404
import re
from django.utils.timezone import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClubName, ClubRep#, MyModel
from .forms import CreateNewUser,RepForm #, MyModelForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# def home(request):
#     return HttpResponse("Hello, Django!")

def index(response, id):
    ls = ClubName.objects.get(id=id)
    return render(response, "hello/accounts.html", {"ls":ls})

def home(response):
    pass
    return render(response, "hello/home.html", {})

def create(response):
    #response.user
    if response.method == "POST":
        form = CreateNewUser(response.POST)
        if form.is_valid():
            n= form.cleaned_data["name"]
            t = ClubName(name=n)
            t.save() 
            #response.user.clubname.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewUser()
    return render(response, "hello/create.html", {"form":form})

def view_reps(response):
    reps_list = ClubRep.objects.all()

    return render(response,"hello/show_list_reps.html", {"reps_list":reps_list} )

def show_rep(response, rep_id):
    rep = ClubRep.objects.get(pk=rep_id)

    return render(response,"hello/show_rep.html", {"rep":rep} )

def update_rep(response, rep_id):
    rep = ClubRep.objects.get(pk=rep_id)
    form = RepForm(response.POST or None, instance=rep)
    if form.is_valid():
        form.save()
        return redirect('clubReps')
    return render(response,"hello/update_rep.html", {'rep': rep,"form":form} )

def delete_rep(reponse, rep_id):
    rep = ClubRep.objects.get(pk=rep_id)
    rep.delete()
    return redirect('clubReps')

def add_reps(response):
    submitted = False
    if response.method == "POST":
        form = RepForm(response.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect("/")
            return HttpResponseRedirect("/addRep?submitted=True")
    else:
        form = RepForm()
        if 'submitted' in response.GET:
            submitted = True
    return render(response,"hello/addRep.html", {'form':form, 'submitted':submitted} )


# def person_update_view(response, pk):
#     person = get_object_or_404(ClubName, pk=pk)
#     form = CreateNewUser(instance=ClubName)
#     if response.method == 'POST':
#         form = CreateNewUser(response.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(response, 'hello/view.html', {'form': form})


def view_clubs(response):
    club_view = ClubName.objects.all()
    return render(response, "hello/view.html", {"club_view":club_view})

def show_club(response, club_id):
    club= ClubName.objects.get(pk=club_id)

    return render(response,"hello/show_club.html", {"club":club} )


def delete_club(reponse, club_id):
    club = ClubName.objects.get(pk=club_id)
    club.delete()
    return redirect('view')
# class CreateMyModelView(CreateView):
#     model = MyModel
#     form_class = MyModelForm
#     template_name = 'hello/create.html'
#     success_url = 'hello/view.html'







# class ClubListView(ListView):
#     model= ClubName


#     def get_context_data(self, **kwargs):
#         context = super(ClubListView, self).get_context_data(**kwargs)
#         return context
#     # def view(response):

#     #     return render(response, "hello/view.html",{})

# def hello_there(request, name):
#     return render(
#         request,
#         '/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )

