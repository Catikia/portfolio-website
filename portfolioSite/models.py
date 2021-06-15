from django.db import models
from django.contrib import admin
#from django.contrib.auth.models import User
from django.urls import reverse
#from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

#Languages used in project
#(This is separate from models so that multiple can be used on each project)
class LanguageOrFramework(models.Model):
    language_or_framework = models.CharField(max_length=100)

    #this def returns the language name instead of index# when model is called
    def __str__(self):
        #"""String for representing the Model object."""
        return self.language_or_framework

# fields in Project
class Project(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200, blank=True, null=True)
    code_link = models.URLField(max_length=250, blank=True, null=True)
    language_or_framework = models.ManyToManyField(LanguageOrFramework)
    summary = models.CharField(max_length=255)
    additional_thoughts = RichTextField(blank=True, null=True)

#InLine allows languages to be edited on same admin page as the project
class ProjectInline(admin.TabularInline):
    model = Project

#InLine allows languages to be edited on same admin page as the project
class LanguageOrFrameworkAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
    ]
