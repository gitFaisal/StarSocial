from django.urls import path
from django.conf.urls import re_path
from .views import (
    PostListView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
)

app_name = 'postsApi'

urlpatterns = [
    path('', PostListView.as_view(), name="list"),
    re_path(r'^(?P<pk>[\w-]+)/detail/$', PostDetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[\w-]+)/edit/', PostUpdateView.as_view(), name="edit"),
    re_path(r'^(?P<pk>[\w-]+)/delete/', PostDeleteView.as_view(), name="delete"),
    # path("new/", views.CreatePost.as_view(), name="create"),
    # path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    # path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    # path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
]
