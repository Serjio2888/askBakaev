from django.shortcuts import render

def new_question(request):
    return render(request, "question/new_question.html", {})

def question(request):
    return render(request, "question/question.html", {})

