from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.new_order, name="new"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
