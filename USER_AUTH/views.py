from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserLoginView(generic.CreateView):
    form_class =UserCreationForm
    template_name = 'Registration/login.html'
    success_url = reverse_lazy('home')
    