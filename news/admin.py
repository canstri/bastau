from django.contrib import admin

# Register your models here.
from .models import Post, Action

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post

class ActionModelAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "object_type", "timestamp"]
    list_display_links = ["user", "title"]
    list_editable = ["object_type"]
    list_filter = ["user", "object_type"]

    search_fields = ["title", "user"]
    class Meta:
        model = Action

admin.site.register(Post, PostModelAdmin)
admin.site.register(Action, ActionModelAdmin)