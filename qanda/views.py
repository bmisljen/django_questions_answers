from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Answer, Question
from django.urls import reverse
from qanda import models
from django.views import generic
from django.utils import timezone

class index(generic.ListView):
    template_name = 'qanda/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]

class detail(generic.DetailView):
    # raise an error if the question does not exist 
    model = Question
    template_name = 'qanda/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def voteup(request):
    """
    Up vote a questions from either the index.html or detail.html templates    
    """
    if request.is_ajax():
        
        question_id = request.GET['question_id']
        question = get_object_or_404(Question, pk=question_id)
        question.votes += 1
        question.save()
        return JsonResponse({'status':'Success', 'msg': 'save successfully'})

    else:
        return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

def votedown(request):
    """
    Down vote a questions from either the index.html or detail.html templates    
    """
    if request.is_ajax():
        
        question_id = request.GET['question_id']
        question = get_object_or_404(Question, pk=question_id)
        question.votes -= 1
        question.save()
        return JsonResponse({'status':'Success', 'msg': 'save successfully'})

    else:
        return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})
    
def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer_text = request.POST.get('answertext')
        if answer_text: 
            # check to make sure that a new answer was entered and then save it 
            answer = models.Answer.objects.create(question=question, 
                                                  answer_text=request.POST.get('answertext'))
            answer.save()
    except (KeyError, Answer.DoesNotExist):
        return HttpResponseRedirect(reverse('qanda:index'))
    
    return HttpResponseRedirect(reverse('qanda:results', args=(question.id,)))

class results(generic.DetailView):
    model = Question
    template_name = 'qanda/results.html'

class displayAddQuestion(generic.ListView):
    model = Question
    template_name = 'qanda/displayAddQuestion.html'

def addQuestion(request):
    question_name=request.POST.get('questionname')
    question_text=request.POST.get('questiontext')
    question = models.Question.objects.create(question_name=question_name,
                                              question_text=question_text,
                                              pub_date=timezone.now(),
                                              votes=0)
    question.save()
    return HttpResponseRedirect(reverse('qanda:index'))