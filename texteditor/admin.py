from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/tinymce/tinymce.min.js',
            '/static/django_tinymce/init_tinymce.js',
            '/static/tinymce_setup.js',
        ]


admin.site.register(models.Post, PostAdmin)
