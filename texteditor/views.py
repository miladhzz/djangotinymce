from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import forms
from django.shortcuts import reverse
from . import models


class Index(generic.CreateView):
    form_class = forms.PostForm
    template_name = "index.html"

    def get_success_url(self):
        return reverse('detail', args=[self.object.id])


class Detail(generic.DetailView):
    model = models.Post
    template_name = "detail.html"
