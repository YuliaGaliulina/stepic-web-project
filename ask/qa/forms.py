from django import forms
from qa.models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
        
    def clean(self):
        return super(AskForm, self).clean()
    
    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self.instance.author
        question.save()
        return question
    
class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def clean(self):
        return super(AnswerForm, self).clean()
    
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author = self.instance.answer
        answer.save()
        return answer
        
