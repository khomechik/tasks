from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'note', 'status', 'importance', 'public', 'created_at', 'deadline')
    fields = (('author', 'title', 'status'), 'note', ('importance', 'public'), 'deadline')
    search_fields = ['title']
    list_filter = ('importance', 'public',)
