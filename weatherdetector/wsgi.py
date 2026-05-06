import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherdetector.settings')

application = get_wsgi_application()  # Required for local Django
app = application                      # Required for Vercel