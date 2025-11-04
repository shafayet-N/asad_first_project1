from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created. Welcome to ContentPro!")
            login(request, user)
            return redirect("orders:dashboard")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
