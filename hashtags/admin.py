from django.contrib import admin

# Register your models here.
from .models import Hashtag

class HashtagModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]

    search_fields = ["name"]
    class Meta:
        model = Hashtag


admin.site.register(Hashtag, HashtagModelAdmin)
