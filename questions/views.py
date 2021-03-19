from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('questions/')

    else:
        # Return an 'invalid login' error message.
        return HttpResponse('felaktiga uppgifter')

def landing(request):
    return HttpResponse('välkommen')

def frontpage(request):
    return HttpResponse('du är inloggad')
