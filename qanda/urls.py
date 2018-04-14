from django.urls import path

from . import views

app_name = 'qanda'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
     # ex: /qanda/5/
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    # ex: /qanda/5/answers/
    path('<int:pk>/results/', views.results.as_view(), name='results'),
    # ex: /qanda/5/answer/
    path('<int:question_id>/answer/', views.answer, name='answer'),
    # ex: /qanda/5/voteup/
    path('voteup/', views.voteup, name='voteup'),
    # ex: /qanda/5/voteup/
    path('votedown/', views.votedown, name='votedown'),
    # ex: /qanda/addquestion/
    path('displayaddquestion/', views.displayAddQuestion.as_view(), name='displayaddquestion'),
    # ex: /qanda/5/addquestion/
    path('addquestion/', views.addQuestion, name='addquestion'), 
    # ex: /qanda/questionsearch/
    path('questionsearch/', views.questionSearch.as_view(), name='questionsearch'),
]