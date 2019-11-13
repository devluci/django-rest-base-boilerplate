import os

from django.core.asgi import get_asgi_application
from rest_base.utils import dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
dotenv.load(os.path.join(os.path.dirname(__file__), '../.env'))

application = get_asgi_application()
