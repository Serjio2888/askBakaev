from django.forms import ModelForm, HiddenInput
# from main.models import Questions, Answers, Users, Rewiews

# class QuestForm(ModelForm):
# 	class Meta:
# 		model = Questions
# 		fields = ['question', 'description', 'author', 'rating', 'creation_time', 'tags', 'views']


from django import forms


class RewiewForm(forms.Form):
    author_nick = forms.CharField(required=True, label="author_nick", max_length=255)
    text = forms.CharField(required=True, label="text")
    author_nick.widget.attrs.update({'class': 'form-control'})
    text.widget.attrs.update({'class': 'form-control'})


class MessageForm(forms.Form):
    email = forms.CharField(required=True,  max_length=255)
    number = forms.CharField(required=True)
    usluga = forms.CharField(required=True)
    problem = forms.CharField(required=True)

    email.widget.attrs.update({'class': 'form-control', "type": "email", "placeholder": "example@mail.ru"})
    number.widget.attrs.update({'class': 'form-control', "placeholder": "+7(977)565-78-41"})
    usluga.widget.attrs.update({'class': 'form-control'})
    problem.widget.attrs.update({'class': 'form-control'})

# from question import models
#
#
# class QuestionForm(forms.Form):
#     question = forms.CharField(required=True, label="Вопрос")
#     description = forms.CharField(label="Подробности вопроса", help_text="put your desc here")
#     tags = forms.CharField(label="Введите теги")
#
#     def clean_name(self):
#         cname = self.cleaned_data['question']
#         if cname.startswith('dick'):
#             raise forms.ValidationError('without dick, pls')
#         return cname
#
#     # def check_pass(self):
#     #     if self.cleaned_data['password'] != self.password:
#     #         print('proverka parolya')
#
#     def save(self):
#         return Questions.objects.create(**form.cleaned_data)
#
#
# class LoginForm(forms.Form):
#     login = forms.CharField(required=True, label="Login")
#     password = forms.CharField(label="Password", max_length=32, widget=forms.PasswordInput)
#
#     def clean_name(self):
#         cname = self.cleaned_data['login']
#         if cname.startswith('dick'):
#             raise forms.ValidationError('without dick, pls')
#         return cname
#
#     def save(self):
#         return Answers.objects.create(**form.cleaned_data)
#
#
# class RegForm(forms.Form):
#     login = forms.CharField(required=True, label="login")
#     password = forms.CharField(required=True, label="Password", max_length=32, widget=forms.PasswordInput)
#     mail = forms.EmailField(required=True, label="email")
#     avatar = forms.ImageField(required=True, label="avatar")
#
#     def save(self):
#         return Answers.objects.create(**form.cleaned_data)
#
#
# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answers
#         fields = [
#             "answer",
#             # "question",
#         ]

