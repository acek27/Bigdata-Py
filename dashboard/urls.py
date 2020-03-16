from django.conf.urls import re_path
from .import views

app_name = "dashboard"
urlpatterns = [
    # re_path(r'^(?P<input>[0-9]+)/$', views.dashboard)
    re_path(r'^$', views.index, name="index"),
]
