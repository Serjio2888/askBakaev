from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from question import forms

from main import models

def main_page(request, questions):
    context = {"test":"roar",
        # 'q_t': models.QuestTag.objects.all(),
        'tags': models.Tags.objects.all(),
        'users': models.Users.objects.all(),
        "questions" : questions,
        "answers" : models.Answers.objects.all()}
    return render(request, "main/index.html", context)

def search_quest(request, query):
    in_desc = models.Questions.objects.filter(description__contains=query)
    in_quest = models.Questions.objects.filter(question__contains=query)
    result = set(in_desc | in_quest)
    if len(result) == 0:
        questions = models.Questions.objects.filter(published=True)
        messages.error(request, 'So sorry, bro. No such questions :(')
        return redirect("index")
    else:
        return main_page(request, result) 

def tag_view(request, tag):
    tag_set = models.Tags.objects.filter(tag=tag)
    if len(tag_set) == 0:
        questions = models.Questions.objects.filter(published=True)
        messages.error(request, 'No such tag, bro :(')
        return redirect("index")
    else:
        tag_id = tag_set[0].id
        questions = models.Questions.objects.filter(published=True, tags=tag_id)
        return main_page(request, questions) 

def newest(request, year=0):
    questions = models.Questions.objects.filter(published=True).order_by("-creation_time")
    return main_page(request, questions)

def popular(request, year=0):
    questions = models.Questions.objects.filter(published=True).order_by("-views")
    return main_page(request, questions)

def index(request, year=0):
    questions = models.Questions.objects.filter(published=True)
    return main_page(request, questions)

def tags(request):
    return render(request, "main/tags.html", {})

def settings(request):
    return render(request, "main/settings.html", {})



    #return HttpResponse('some_text')#content-type="text/plain"
