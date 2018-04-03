from django import forms

from .models import Problem
from django.forms import CharField


class SaveProblemForm(forms.ModelForm):
    expr1 = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':1, 'cols':25}), required=False)
    expr2 = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':1, 'cols':25}), required=False)
    class Meta:
        model = Problem
        fields = [
            "expr1",
            "expr2",
        ]