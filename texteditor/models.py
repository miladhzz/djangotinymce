from django.db import models
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True)


