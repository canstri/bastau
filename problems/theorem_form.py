from django import forms

from .models import Theorem
from django.forms import CharField


class TheoremForm(forms.ModelForm):
    expr1 = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':3, 'cols':50}), required=False)
    class Meta:
        model = Theorem
        fields = [
            "expr1",
        ]