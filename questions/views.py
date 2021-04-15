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

class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, DedupMessageMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = 'home'
    template_name = 'questions/createquestion.html'

    def post(self, request):
        profile = Profile.objects.get(user = request.user)
        badges_before = profile.get_badges()
        messages.success(request, "hello")
        super(QuestionCreateView, self).post(request)
        badges_after = profile.get_badges()
        gained_points = profile.points - profile.previous_points
        if profile.group:
            messages.success(request, "Your question was successfully added!" + "\n" + "You gained " + str(gained_points) + " points")
            for index in range (6):
                if badges_after[index] != badges_before[index]:
                    messages.success(request, "You recieved a badge! Check it out in your profile")
        else:
            messages.success(request, "Your question was successfully added!")
        return HttpResponseRedirect(reverse_lazy('home'))
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def QuestionSuccess(request):
    profile = Profile.objects.get(user = request.user)
    return profile.get_gained_points
    
    
