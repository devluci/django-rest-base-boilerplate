from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
]

for app in settings.APPS:
    urlpatterns.append(re_path(f'{app}(?:$|/)', include(f'{app}.urls'), name=app))
