from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WriterProfile
from .forms import WriterProfileForm

@login_required
def edit_profile(request):
    profile, _ = WriterProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = WriterProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your writer profile has been updated.")
            return redirect("writers:profile")
    else:
        form = WriterProfileForm(instance=profile)
    return render(request, "writers/profile_form.html", {"form": form})

@login_required
def view_profile(request):
    profile, _ = WriterProfile.objects.get_or_create(user=request.user)
    return render(request, "writers/profile_detail.html", {"profile": profile})
