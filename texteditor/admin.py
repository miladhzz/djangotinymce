from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/filebrowser/js/tinymce_setup.js',
        ]


admin.site.register(models.Post, PostAdmin)
