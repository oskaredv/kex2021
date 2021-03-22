from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def landing(request):
    return HttpResponse('välkommen')

def frontpage(request):
    return HttpResponse('du är inloggad')
