from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from .models import Question, Profile
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateQuestionForm
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .mixin import DedupMessageMixin

class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'questions/viewprofile.html'

    def get_object(self):
        return get_object_or_404(Profile, user = self.request.user) 

class LeaderboardView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'questions/viewleaderboard.html'

    def get_queryset(self, *args, **kwargs):
        profiles = super(LeaderboardView, self).get_queryset(*args, **kwargs)
        profiles = profiles.order_by("-points")[:10]
        return profiles

class QuestionCreateView(SuccessMessageMixin,LoginRequiredMixin, DedupMessageMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = reverse_lazy('home')
    template_name = 'questions/createquestion.html'

    def get_success_message(self, cleaned_data):
        profile = Profile.objects.get(user=self.object.user)
        gained_points = profile.points - profile.previous_points
        badge_message = ""
        if profile.group:
            if profile.just_gainded_badge:
                badge_message = "You also recieved a badge which gave you some additional points, check it out in your profile!"
            return "You gained " + str(gained_points) + " points for submitting this question!" +"\n"+ badge_message
        else: 
            return "Your question was successfully added!"
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def QuestionSuccess(request):
    profile = Profile.objects.get(user = request.user)
    return profile.get_gained_points
    
    
