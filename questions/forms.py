from django.forms import ModelForm
from django import forms
from .models import Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Div, Layout, Field

class CreateQuestionForm(ModelForm):
    question_text = forms.CharField(label='Question text', help_text='Write your question here', widget = forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Field('question_text', wrapper_class= 'col-xs-6', css_class = 'row-fluid')
            ))

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