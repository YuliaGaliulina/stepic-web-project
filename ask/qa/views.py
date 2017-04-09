from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from qa.models import QuestionManager, Question
from django.core.paginator import Paginator

class QuestionNewList(ListView):

    template_name = 'question_list.html'
    model = Question
    paginate_by = 10
    
    def get_queryset(self):
        return Question.objects.new()

    
class QuestionPopularList(ListView):
    
    template_name = 'question_list.html'
    model = Question
    paginate_by = 10
        
    def get_queryset(self):
        return Question.objects.popular()


class QuestionDetail(DetailView):
    
    template_name = 'question_detail.html'
    model = Question

    
def test(request, *args, **kwargs):
    return HttpResponse('OK')
