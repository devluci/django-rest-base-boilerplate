from django.urls import re_path
from rest_base.urls import method_branch

from . import views

urlpatterns = [
    re_path(r'^me/?$', method_branch(GET=views.about_me)),
]
