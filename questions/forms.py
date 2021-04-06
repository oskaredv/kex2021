from django.forms import ModelForm
from .models import Question

class CreateQuestionForm(ModelForm):

    def save(self, *args, **kwargs):
        if CreateQuestionForm.is_valid():
            #obj = super(ModelForm, self).save(*args, **kwargs)
            question = super().save(user=self.request.user, COMMIT=False)
            #if self.request:
            #    obj.user = self.request.user
                #user = User.objects.get(username=request.user.username)
            question.save()
            return redirect('createquestion')

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