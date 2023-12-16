from datetime import datetime, timedelta

from django.contrib import admin
from .models import LevelType, LevelOrganization


@admin.register(LevelType)
class LevelTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'created_at', 'updated_at', 'name_ru', 'name_en', 'name_uz', 'name_oz', 'color')


@admin.register(LevelOrganization)
class LevelOrganizationAdmin(admin.ModelAdmin):
    fields = ('level', 'organization')
    list_display = ('level', 'organization', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    # how to update created_at and updated_at fields?

    def save_model(self, request, obj, form, change):
        obj.created_at = datetime.now() - timedelta(days=8)
        obj.updated_at = datetime.now()
        super().save_model(request, obj, form, change)