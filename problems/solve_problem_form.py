from django import forms

from .models import Problem
from django.forms import CharField


class CheckProblemForm(forms.ModelForm):
    expr1 = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':3, 'cols':103}), required=False)
    class Meta:
        model = Problem
        fields = [
            "expr1",
        ]