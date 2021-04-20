from django import forms
from . import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
        widgets = {
            'content': SummernoteInplaceWidget(),
        }
