from django import forms

from .models import Comment
from django.forms import CharField



class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'cols':25}))
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
