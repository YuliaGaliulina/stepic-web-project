from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Question
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import resolve_url, redirect
from .forms import AskForm, AnswerForm
from django.core.urlresolvers import reverse

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


class AnswerView(CreateView):

    form_class = AnswerForm
    template_name = 'question_detail.html'

    
class QuestionDetail(DetailView, AnswerView):
    
    template_name = 'question_detail.html'
    model = Question
    form_class = AnswerForm
    success_url = '/'

    def get_context_data(self, **kwargs):   
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['form'] = AnswerForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if self.request.user:
                form.instance.author = self.request.user
            else:
                form.instance.author = "Anonymous"
            form.instance.question = Question.objects.get(pk=self.kwargs['pk'])
        super(AnswerView, self).form_valid(form)
        return redirect(self.request.path) 

class AskCreate(CreateView):
    
    form_class = AskForm
    template_name = 'ask.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AskCreate, self).form_valid(form)
    
    def get_success_url(self):
        return resolve_url('question_detail', pk=self.object.pk)


