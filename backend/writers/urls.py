from django.urls import path
from . import views

urlpatterns = [
    path("profile/edit/", views.edit_profile, name="profile_edit"),
    path("profile/", views.view_profile, name="profile"),
]
