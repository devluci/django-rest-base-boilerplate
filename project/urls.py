from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

if settings.ADMIN_PREFIX:
    admin_endpoint = settings.ADMIN_PREFIX + '/admin/'
else:
    admin_endpoint = 'admin/'

urlpatterns = [
    path(admin_endpoint, admin.site.urls),
]

for app in settings.APPS:
    urlpatterns.append(re_path(f'{app}(?:$|/)', include(f'{app}.urls'), name=app))
