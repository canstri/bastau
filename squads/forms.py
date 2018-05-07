from django import forms
from pagedown.widgets import PagedownWidget
from .models import Squad
from django.forms import CharField


class SquadForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview = False))
    class Meta:
        model = Squad
        fields = [
            "title",
            "content",
            "image",
        ]