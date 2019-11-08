from django.forms import ModelForm, HiddenInput
from main.models import Questions, Answers

class QuestForm(ModelForm):
	class Meta:
		model = Questions
		fields = ['question', 'description', 'author', 'rating', 'creation_time', 'tags', 'views']

