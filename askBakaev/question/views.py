# from django.shortcuts import render, HttpResponse, redirect
# from django.views.generic.detail import DetailView
# from django.contrib import messages
#
# from question import forms
#
# from main.models import Questions, Answers, Tags, Users
#
# def new_question(request):
#     if request.method == "POST":
#         # print(request)
#         # messages.success(request, 'Your question was added succesfully!')
#         messages.warning(request, "Your question was not added")
#         # pk = Questions.objects.all()[-1].id
#         pk = 1
#         return redirect("question", pk)
#     return render(request, "question/new_question.html", {'form':forms.QuestionForm()})
#
# # def question(request, pk):
# #     print("hello", pk)
# #     if request.method == 'POST':
# #         # simply return a string that shows the IDs of selected items
# #         print("here we are")
# #         messages.success(request, 'Your password was updated successfully!')
# #         return HttpResponse('<br />'.join(request.POST.getlist('choices')))
#
# def answer(request, pk):  # pk is for question num
#     question = Questions.objects.filter(pk=pk)[0]
#     if request.method == "POST":
#         messages.success(request, 'Your answer was added succesfully!')
#         return redirect("question", pk)
#     return render(request, "question/new_answer.html", {'question':question,
#                                                         'form':forms.AnswerForm()})
#
# class QuestView(DetailView):
#     model = Questions
#     template_name = 'question/question.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         if True:
#                 q = Questions.objects.get(pk=context['questions'].id)
#                 q.views += 1
#                 q.save()
#         context['increment'] = Questions.objects.increment(context['object'])
#         #print(context['questions'].__dict__)
#         #context['comment_add_url'] = "/topic/{}/add_comment".format(context['topic'].id)
#         return context
#
