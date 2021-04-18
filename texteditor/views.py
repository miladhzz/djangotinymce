from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import forms


class Index(generic.CreateView):
    form_class = forms.PostForm
    template_name = "index.html"
    success_url = "/"
