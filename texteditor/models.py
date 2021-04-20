from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()

