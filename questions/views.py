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

class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'questions/viewprofile.html'

    def get_object(self):
        #return Profile.objects.get(self.request.user)
        return get_object_or_404(Profile, user = self.request.user)
    
    '''def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        #context['questions'] = Question.objects.filter(user__username__iexact=self.kwargs.get('username'))
        return context'''  

class LeaderboardView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'questions/viewleaderboard.html'

    def get_queryset(self, *args, **kwargs):
        profiles = super(LeaderboardView, self).get_queryset(*args, **kwargs)
        profiles = profiles.order_by("-points")[:10]
        return profiles

class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = reverse_lazy('createquestion')
    success_message = "Your question was successfully added! %(gamification_message)"
    template_name = 'questions/createquestion.html'

    def get_success_message(self):
        profile = Profile.objects.get(user=self.user)
        gained_points = profile.points - profile.previous_points
        if profile.group:
            #return self.success_message + "You gained " + % (gamification_message = gained_points) + " Good job!"
            return self.success_message % (gamification_message = "You gained " + gained_points + " points")
        else: 
            return self.success_message % (gamification_message = "")


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def QuestionSuccess(request):
    profile = Profile.objects.get(user = request.user)
    return profile.get_gained_points
    
    
