from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from polls.models import Question,Choice


# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {"questions":questions}
    return render(request,"index.html",context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {"question":question}
    return render(request,"detail.html",context)

def results(request,question_id):
    response = "estas viendo los resultados %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("voto realizado %s." % question_id)