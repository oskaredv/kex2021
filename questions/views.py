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

def landing(request):
    return HttpResponse('välkommen')

def frontpage(request):
    return HttpResponse('du är inloggad')

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


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = reverse_lazy('createquestion')
    template_name = 'questions/createquestion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
