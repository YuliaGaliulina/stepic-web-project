from django.conf.urls import url
from . import views
from .views import QuestionNewList, QuestionPopularList, QuestionDetail


urlpatterns = [
    url(r'^login/', views.test, name='login'),
    url(r'^signup/', views.test, name='signup'),
    url(r'^ask/', views.test, name='ask'),
    url(r'^$', QuestionNewList.as_view(), name='new'),
    url(r'^popular/', QuestionPopularList.as_view(), name='popular'),
    url(r'^question/(?P<pk>\d+)/$', QuestionDetail.as_view(), name='question_detail'),
   
    
]

