from django.contrib import admin

# Register your models here.
from .models import Task

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["title"]

    search_fields = ["title", "content"]
    class Meta:
        model = Task

admin.site.register(Task, TaskModelAdmin)