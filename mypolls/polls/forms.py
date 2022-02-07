from django.forms import ModelForm
from .models import Poll, Option
from django import forms
from django.forms import formset_factory

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['id', 'question', 'type', 'description' ]

class TextOptionForm(forms.Form):
    text = forms.CharField(
        label='Option Text',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Option here'
        })
    )
OptionFormSet = formset_factory(TextOptionForm, extra=1)
