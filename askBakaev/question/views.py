from django.shortcuts import render
from django.views.generic.detail import DetailView

from main.models import Questions, Answers, Tags, Users

def new_question(request):
    return render(request, "question/new_question.html", {})

# def question(request):
#         context = {"test":"roar",
#         # 'q_t': models.QuestTag.objects.all(),
#         'tags': models.Tags.objects.all(),
#         'users': models.Users.objects.all(),
#         "questions" : models.Questions.objects.all(),
#         "answers" : models.Answers.objects.all()}
#     return render(request, "question/question.html", {})

class QuestView(DetailView):
    model = Questions
    template_name = 'question/question.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        if True:
                q = Questions.objects.get(pk=context['questions'].id)
                q.views += 1
                q.save()
        context['increment'] = Questions.objects.increment(context['object'])
        #print(context['questions'].__dict__)
        #context['comment_add_url'] = "/topic/{}/add_comment".format(context['topic'].id)
        return context

