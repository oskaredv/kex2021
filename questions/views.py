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
        return Profile.objects.get(self.request.user.id)
        #return get_object_or_404(Profile, self.request.user.id)
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        #context['questions'] = Question.objects.filter(user__username__iexact=self.kwargs.get('username'))
        return context  


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = CreateQuestionForm
    success_url = reverse_lazy('createquestion')
    template_name = 'questions/createquestion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



'''def QuestionCreateView(request):
    if request.method == 'POST':
        question_form = forms.CreateQuestionForm(request.POST)
        if question_form.is_valid()
            question = question_form.save(commit=False)
            question.user = request.user
            question.save()
            
            

            
            phone=phone_form.save(False)
            phone.farm = farm
            phone.save()
            address = address_form.save(False)
            address.farm = farm
            address.save()
            
            question_text=
            
    farm_form = forms.CreateFarmsForm()
    phone_form = forms.TelephoneCreateForm()
    address_form = forms.AddressCreateForm()
    context = {'farm_form':farm_form, 'phone_form':phone_form, 'address_form':address_form,}
    return render(request, "livestock/farm_name.html", context)
    
    question_form = forms.CreateQuestionForm()
    choice_form = forms.CreateChoiceForm()
    context = {'question_form':question_form, 'choice_form':choice_form,}
    return render(request, "questions/createquestion.html", context)'''
    
    
