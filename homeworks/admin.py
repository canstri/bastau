from django.contrib import admin

# Register your models here.
from .models import Homework

class HomeworkModelAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = Homework

admin.site.register(Homework, HomeworkModelAdmin)