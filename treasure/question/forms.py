# forms.py
from django import forms
from .models import Question

class DynamicAnswerForm(forms.Form):
    name = forms.CharField(label='Your Team Name', max_length=100)

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)

        for question in questions:
            self.fields[f'answer_{question.id}'] = forms.CharField(
                label=question.question,
                widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'})
            )
