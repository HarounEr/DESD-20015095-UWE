from django.urls import path
from hello.models import ClubName
from hello import views

# home_list_view = views.HomeListView.as_view(
#     queryset=ClubName.objects,  # :5 limits the results to the five most recent
#     context_object_name="message_list",
#     template_name="hello/view.html",
# )

urlpatterns = [
    #path("", views.home, name="home"),
    #path("", views.hello_there, name = "hello_there"),
    path("<int:id>",views.index, name="index"),
    path("",views.home, name="home"),
    path("create/",views.create, name="create"),
    path("view/",views.view_clubs, name="view"),
    path("show_club/<club_id>",views.show_club, name="showClub"),
    path("show_list_reps/",views.view_reps, name="clubReps"),
    path("addRep/",views.add_reps, name="AddReps"),
    path("show_rep/<rep_id>",views.show_rep, name="showRep"),
    path("update_rep/<rep_id>",views.update_rep, name="updateRep"),
    path("delete_rep/<rep_id>",views.delete_rep, name="deleteRep"),
    path("delete_club/<club_id>",views.delete_club, name="deleteClub"),
   
    #path("delete/<clubRep_id>", views.deleteRep, name='delete')
]