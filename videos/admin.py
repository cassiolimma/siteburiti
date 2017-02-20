from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ['title', 'link', 'slug', 'date_post', 'created_at']
	search_fields = ['title', 'link', 'text']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Video, VideoAdmin)
