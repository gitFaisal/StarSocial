from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # reverse_lazy allows us to redirct after signing up
    # where as reverse would just redirect before they could do that.
    success_url = reverse_lazy('login')

    template_name = 'accounts/signup.html'
