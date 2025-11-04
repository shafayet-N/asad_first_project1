from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")

def enterprise_domain(request):
    return render(request, "enterprise-domain.html")

def pricing(request):
    return render(request, "pricing.html")

def for_writers(request):
    return render(request, "for_writers.html")

def client_dashboard(request):
    return render(request, "client-dashboard.html")

def order_content(request):
    return render(request, "order_content.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def writer_dashboard(request):
    return render(request, "writer-dashboard.html")
    

def admin_dashboard(request):
    return render(request, "admin-dashboard.html")