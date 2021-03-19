from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login

def landing(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('questions/')

    else:
        # Return an 'invalid login' error message.
        HttpResponse('felaktiga uppgifter')


def frontpage(request):
    HttpResponse(du är inloggad)
