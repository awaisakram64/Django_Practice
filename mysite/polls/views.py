from django.http import HttpResponse, Http404, HttpResponseRedirect
# Commit below line as 1 method
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))