from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import forms
from . import models


class Index(generic.CreateView):
    form_class = forms.PostForm
    template_name = "index.html"
    success_url = "/"


class Detail(generic.DetailView):
    model = models.Post
    template_name = "detail.html"
