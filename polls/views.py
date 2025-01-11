from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Choice, Question

# Create your views here.


def index(request):
    # return HttpResponse("Hello world! Welcome to my django app!")
    questions = Question.objects.all()
    # return HttpResponse(questions)
    return render(request, "polls/index.html", {"questions": questions})


def detail(request, id):
    # return HttpResponse(f"Question {id}")
    try:
        question = Question.objects.get(id=id)
    except Exception as e:
        # question = Question.objects.all()[0]
        raise Http404(e)
    else:
        return render(request, "polls/detail.html", {"question": question})


def results(request, id):
    return HttpResponse(f"Results for question {id}")


def vote(request, id):
    return HttpResponse(f"Voting page for question {id}")
