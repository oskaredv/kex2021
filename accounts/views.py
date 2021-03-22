from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from accounts.forms import UserForm

from django.contrib.auth import authenticate, login

def login(request):
    template = loader.get_template('accounts/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('questions/')

    else:
        # Return an 'invalid login' error message.
        return HttpResponse('felaktiga uppgifter')


class SignUpView(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

