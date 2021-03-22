# accounts/urls.py
from django.urls import path
from django.http import HttpResponse
from .views import SignUpView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.login, name='login')
]