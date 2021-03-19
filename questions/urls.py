from django.urls import path


from . import views

urlpatterns = [
    path('', views.firstpagetest, name='firstpagetest')
]
