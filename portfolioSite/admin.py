from django.contrib import admin
from .models import Project, LanguageOrFramework, ProjectInline, LanguageOrFrameworkAdmin

# Register your models here.
admin.site.register(Project)
admin.site.register(LanguageOrFramework)
#admin.site.register(ProgrammingLanguageInline)
#admin.site.register(AuthorAdmin)
