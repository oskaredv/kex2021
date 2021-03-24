from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from accounts.forms import UserForm
from django.http import HttpResponse

from django.contrib.auth import authenticate, login



class SignUpView(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

