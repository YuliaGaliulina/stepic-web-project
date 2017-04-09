from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

    
class Question(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()
    title = models.CharField(max_length=200)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='question_like_user')
    objects = QuestionManager()
    
    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.text

