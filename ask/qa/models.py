from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.filter(added_at__lte=auto_now_add())
    def popular(self):
        return self.filter(rating__gt)

class Question(models.Model):
    objects = QuestionManager()
    author = models.ForeignKey(User)
    text = models.TextField()
    title = models.CharField(max_length=200)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='question_like_user')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


