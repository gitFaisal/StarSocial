from django.urls import path
from django.conf.urls import re_path
from .views import GroupListAPI, GroupDetailAPI

app_name = "groupsApi"

urlpatterns = [
        path('', GroupListAPI.as_view(), name="groupList" ),
        re_path(r'^(?P<pk>[\w-]+)/edit/$', GroupDetailAPI.as_view(), name="groupEdit"),


]
