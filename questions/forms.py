from django.forms import ModelForm
from .models import Question

class CreateQuestionForm(ModelForm):
    
    class Meta:
        model = Question
        fields = ['question_text', 
                  'choice_a',
                  'choice_a_correct', 
                  'choice_b',
                  'choice_b_correct', 
                  'choice_c', 
                  'choice_c_correct',
                  'choice_d',
                  'choice_d_correct']
    


'''
class CreateChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'correct_choice']
'''