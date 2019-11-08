from django.shortcuts import render

# Create your views here.

from main import models

def index(request, year=0):
    context = {"test":"roar",
        # 'q_t': models.QuestTag.objects.all(),
        'tags': models.Tags.objects.all(),
        'users': models.Users.objects.all(),
        "questions" : models.Questions.objects.all(),
        "answers" : models.Answers.objects.all()}
    return render(request, "main/index.html", context)

def tags(request):
    return render(request, "main/tags.html", {})

def settings(request):
    return render(request, "main/settings.html", {})


    #return HttpResponse('some_text')#content-type="text/plain"
