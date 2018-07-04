from django.urls import path

from . import views

app_name = "display"
urlpatterns = [
    # /display/
    path("", views.index, name="index"),

    # /display/4
    path("<int:question_id>/", views.details, name="details"),

    # /display/4/results/
    path("<int:question_id>/results/", views.results, name="results"),

    # /display/4/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # /display/person/1
    path("member/<int:member_id>", views.display_member, name="vote"),
]

