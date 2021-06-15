from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, LanguageOrFramework, ProjectInline, LanguageOrFrameworkAdmin

#this is the view for the home page
class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    languages = LanguageOrFramework.objects.all()
    ordering = ['-id']
