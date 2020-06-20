from django.urls import path
from django.conf.urls import url
from . import views
app_name ='polls'
urlpatterns =[
  # /posts

  path('' , views.index , name = 'index'),
  # /posts/question_id
  path('<int:question_id>/', views.detail , name ='detail'),
  # /posts / question_id /results
  path('<int:question_id>/results/'  , views.results , name='results'),
  # /posts / question_id /vote
  path('<int:question_id>/vote/' , views.vote , name = 'vote')
];
