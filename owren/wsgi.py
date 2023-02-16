"""
WSGI
"""

import os
# from django_forest import init_forest
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'owren.settings')

# init_forest()
application = get_wsgi_application()