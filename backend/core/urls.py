from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("enterprise-domain/", views.enterprise_domain, name="enterprise_domain"),
    path("pricing/", views.pricing, name="pricing"),
    path("for-writers/", views.for_writers, name="for_writers"),
    path("client-dashboard/", views.client_dashboard, name="client_dashboard"),
    path('writer-dashboard/', views.writer_dashboard, name="writer_dashboard"),   
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),     
    path("order-content/", views.order_content, name="order_content"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
]
