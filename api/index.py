import os
import sys
from pathlib import Path

# Add backend to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / 'backend'
sys.path.insert(0, str(BACKEND_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Setup Django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

# Vercel serverless handler
def handler(request):
    return app(request)
