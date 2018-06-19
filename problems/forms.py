from django import forms

from .models import Problem
from django.forms import CharField


class CreateProblemForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(label='', widget=forms.Textarea)
    hashtags = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':25}))
    level = forms.IntegerField()
    class Meta:
        model = Problem
        fields = [
            "title",
            "content",
            "level",
        ]