# Generated by Django 3.1.5 on 2021-04-20 03:26

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('texteditor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image'),
        ),
    ]
