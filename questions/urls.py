from django.urls import path


from . import views

urlpatterns = [
    path('questions/', views.frontpage, name='frontpage'),
    path('', views.landing, name='landing')
]
