from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_filter = ('region', 'district', 'state', 'category', 'specialization')
    search_fields = ('fullname', 'shortname', 'address')
    list_per_page = 20
