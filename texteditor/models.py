from django.db import models
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])
