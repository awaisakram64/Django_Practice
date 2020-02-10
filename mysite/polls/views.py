from django.http import HttpResponse, Http404
# Commit below line as 1 method
# from django.template import loader
from django.shortcuts import render
from .models import Question, Choice


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Commit below line as 1 method
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request, 'polls/index.html', context)
    # Commit below line as 1 method
    # return HttpResponse(template.render(context,request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Does not exits")
    return render(request, 'polls/detail.html', {'question':question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)