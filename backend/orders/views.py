from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import Order

@login_required
def new_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, "Your content order has been submitted.")
            return redirect("orders:dashboard")
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_list.html", {"orders": orders})
