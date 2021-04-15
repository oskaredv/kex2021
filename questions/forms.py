from django.forms import ModelForm
from .models import Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Div, Layout

class CreateQuestionForm(ModelForm):
    question_text = forms.CharField(label='questiontext', help_text='This is your question', widget = forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Field(question_text), wrapper_class= 'col-md-6', css_class = 'row-fluid'),
            ),
            Row(
                Field('choice_a', wrapper_class= 'col-md-6', css_class = 'row-fluid'),
                Field('choice_a_correct', wrapper_class= 'col-md-6', css_class = 'row-fluid')
            ),
            Row(
                Field('choice_b', wrapper_class= 'col-md-6', css_class = 'row-fluid'),
                Field('choice_b_correct', wrapper_class= 'col-md-6', css_class = 'row-fluid')
            ),
            Row(
                Field('choice_c', wrapper_class= 'col-md-6', css_class = 'row-fluid'),
                Field('choice_c_correct', wrapper_class= 'col-md-6', css_class = 'row-fluid')
            ),
            Row(
                Field('choice_d', wrapper_class= 'col-md-6', css_class = 'row-fluid'),
                Field('choice_d_correct', wrapper_class= 'col-md-6', css_class = 'row-fluid')
            ),
        )

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