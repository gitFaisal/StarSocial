from django.conf.urls import url
# Django handles login and logout by import the following:
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # We are using our own login view for the first one
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    # Using default logout view from django
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    # Using the sign up view we have set up in this directory
    url(r'signup/$',views.SignUp.as_view(),name='signup'),

]
