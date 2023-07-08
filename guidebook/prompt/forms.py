from django import forms

from .models import Prompt

class PromptFilterForm(forms.Form):
    language = forms.ChoiceField(choices=Prompt.LANGUAGE_CHOICES, required=False)
    category = forms.ChoiceField(choices=Prompt.CATEGORY_CHOICES, required=False)
    difficulty = forms.ChoiceField(choices=Prompt.DIFFICULTY_CHOICES, required=False)
    