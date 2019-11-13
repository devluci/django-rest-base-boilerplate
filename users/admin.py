from django.contrib import admin
from rest_base.admin import model_admin

from .models import *

admin.site.register(*model_admin(User))
