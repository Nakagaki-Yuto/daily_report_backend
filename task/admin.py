from django.contrib import admin
from .models import Task
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Task, MarkdownxModelAdmin)
