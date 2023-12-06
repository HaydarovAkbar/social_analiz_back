from django.contrib import admin
from . import models


admin.site.register(models.SocialTypes)

@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_filter = ('link', 'state', 'social_type', 'organization')
    search_fields = ('link', 'integration_id')
    list_per_page = 20


@admin.register(models.SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_filter = ('post_date', 'organization', 'social_type')
    search_fields = ('url', 'social_type')
    list_per_page = 50


@admin.register(models.SocialPostStats)
class SocialPostStatsAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'social')
    search_fields = ('post', 'social')
    list_per_page = 100
