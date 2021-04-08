from django.urls import path
from .views import QuestionCreateView, ProfileView, LeaderboardView
from . import views

urlpatterns = [
    path('createquestion/', QuestionCreateView.as_view(), name='createquestion'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]
