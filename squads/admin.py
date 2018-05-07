from django.contrib import admin

# Register your models here.
from .models import Squad

class SquadModelAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title"]
    list_filter = ["title"]

    search_fields = ["content"]
    class Meta:
        model = Squad

admin.site.register(Squad, SquadModelAdmin)
