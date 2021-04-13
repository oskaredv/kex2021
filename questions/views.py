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

class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, DedupMessageMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = reverse_lazy('createquestion')
    success_message = "Testing"
    #success_message = "Your question was successfully added!"
    template_name = 'questions/createquestion.html'

    def post(self, request):
        super(QuestionCreateView, self).post(request)
        profile = Profile.objects.get(user = request.user)
        gained_points = profile.points - profile.previous_points
        if profile.group:
            messages.success(request, "Your question was successfully added!" + "\n" + "You gained " + str(gained_points) + " points")
        else:
            messages.success(request, "Your question was successfully added!")
        return HttpResponseRedirect(reverse_lazy('createquestion'))
        
        '''post_data = request.POST or None
        #file_data = request.FILES or None

        question_form = CreateQuestionForm(post_data, instance = request.user)

        if question_form.is_valid():
            question_form.save()
            
            

        context = self.get_context_data(question_form=question_form)

        return self.render_to_response(context)


    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)''' 
        
              
    def get_success_message(self, cleaned_data):
        profile = Profile.objects.get(user=self.object.user)
        gained_points = profile.points - profile.previous_points
        if profile.group:
            return "Your question was successfully added!" + "\n" + "You gained " + str(gained_points) + " points"
        else: 
            return "Your question was successfully added!"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def QuestionSuccess(request):
    profile = Profile.objects.get(user = request.user)
    return profile.get_gained_points
    
    
