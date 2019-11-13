import os

from django.core.wsgi import get_wsgi_application
from rest_base.utils import dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
dotenv.load(os.path.join(os.path.dirname(__file__), '../.env'))

application = get_wsgi_application()
