from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App URLs
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('writers/', include('writers.urls')),
    
    # Core/main app routes
    path('', include('core.urls')),
]

# Fallback for 404s (optional)
handler404 = 'django.views.defaults.page_not_found'
