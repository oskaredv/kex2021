from django.urls import path
from .views import QuestionCreateView
from . import views

urlpatterns = [
    path('questions/', views.frontpage, name='frontpage'),
    path('createquestion/', QuestionCreateView.as_view(), name='createquestion')
]
