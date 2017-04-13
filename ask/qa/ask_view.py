from django.shortcuts import resolve_url
from qa.models import Question


class AskCreate(CreateView):
    model = Question
    template_name = 'ask.html'
    fields = ('title', 'text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AskCreate, self).form_valid(form)
    
    def get_success_url(self):
        return resolve_url('question_detail', pk=self.object.pk)
