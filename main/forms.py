from django import forms
from main.models import Answer
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']

