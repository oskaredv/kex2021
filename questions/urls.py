from django.urls import path
from .views import QuestionCreateView, ProfileView
from . import views

urlpatterns = [
    path('questions/', views.frontpage, name='frontpage'),
    path('createquestion/', QuestionCreateView.as_view(), name='createquestion'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
