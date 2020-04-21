from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from question import forms

from main import models


def main_page(request):
    context = {"Mform": forms.MessageForm}
    if request.method == 'POST':
        send_message(request)
        context["ok"] = True
    return render(request, "main/index.html", context)


def index(request, year=0):
    return main_page(request)


def team(request, year=0):
    context = {"Mform": forms.MessageForm}
    if request.method == 'POST':
        send_message(request)
        context["ok"] = True

    return render(request, "main/team.html", context)


def practice(request, year=0):
    context = {"Mform": forms.MessageForm}
    if request.method == 'POST':
        send_message(request)
        context["ok"] = True
    return render(request, "main/practice.html", context)


def send_message(request):
    m_form = forms.MessageForm(request.POST)
    mail = m_form.data["email"]
    number = m_form.data["number"]
    problem = m_form.data["problem"]
    msg = models.Messages(email=mail, number=number, text=problem)
    msg.save()


def reviews(request, year=0):
    context = {"Rform": forms.RewiewForm,
               "Mform": forms.MessageForm,
               "comm": False,
               "rewiews": models.Rewiews.objects.all(),
               "ok": False}
    if request.method == 'POST':
        form = forms.RewiewForm(request.POST)
        if not form.data.get('author_nick'):
            send_message(request)
            context["ok"] = True
        else:
            author_nick = form.data['author_nick']
            text = form.data['text']
            rew = models.Rewiews(author_nick=author_nick, text=text)
            rew.save()
            context["comm"] = True
    context["msg"] = forms.MessageForm
    return render(request, "main/reviews.html", context)


def tags(request):
    return render(request, "main/tags.html", {})


def settings(request):
    return render(request, "main/settings.html", {})





#
# def tag_view(request, tag):
#     tag_set = models.Tags.objects.filter(tag=tag)
#     if len(tag_set) == 0:
#         questions = models.Questions.objects.filter(published=True)[:10]
#         messages.error(request, 'No such tag, bro :(')
#         return redirect("index")
#     else:
#         tag_id = tag_set[0].id
#         questions = models.Questions.objects.filter(published=True, tags=tag_id)[:10]
#         return main_page(request, questions)
#
#
# def newest(request, year=0):
#     questions = models.Questions.objects.filter(published=True).order_by("-creation_time")[:10]
#     return main_page(request, questions)
#
#
# def popular(request, year=0):
#     questions = models.Questions.objects.filter(published=True).order_by("-views")[:10]
#     return main_page(request, questions)
#
#
# def search_quest(request, query):
#     in_desc = models.Questions.objects.filter(description__contains=query)
#     in_quest = models.Questions.objects.filter(question__contains=query)
#     result = set(in_desc | in_quest)
#     if len(result) == 0:
#         questions = models.Questions.objects.filter(published=True)[:10]
#         messages.error(request, 'So sorry, bro. No such questions :(')
#         return redirect("index")
#     else:
#         return main_page(request, result)
