from django.conf.urls import re_path
from .import views

urlpatterns = [
    # re_path(r'^(?P<input>[0-9]+)/$', views.dashboard)
    re_path(r'^$', views.dashboard , name="dashboard")
]
