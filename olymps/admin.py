from django.contrib import admin

# Register your models here.
from .models import Olymp, RatingOlymp

class OlympModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp"]
	list_display_links = ["title"]
	list_filter = ["timestamp"]

	search_fields = ["title"]
	class Meta:
		model = Olymp


admin.site.register(Olymp, OlympModelAdmin)

class RatingOlympModelAdmin(admin.ModelAdmin):
    list_display = ["olymp"]
    list_display_links = ["olymp"]
    list_filter = ["olymp"]

    search_fields = ["olymp"]
    class Meta:
        model = RatingOlymp


admin.site.register(RatingOlymp, RatingOlympModelAdmin)