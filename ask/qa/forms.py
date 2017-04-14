from django import forms
from qa.models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
        
