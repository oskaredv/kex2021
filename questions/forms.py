from django.forms import ModelForm
from .models import Question

class CreateQuestionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super().__init__(*args, **kwargs)


    def save(self, *args, **kwargs):
        kwargs['commit']=False
        #obj = super(ModelForm, self).save(*args, **kwargs)
        obj = super().save(*args, **kwargs)
        if self.request:
            obj.user = self.request.user
        obj.save()
        return obj

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