from django.contrib import admin
from .models import FileStatus, TelevisionType, Files


admin.site.register(FileStatus)
admin.site.register(TelevisionType)

@admin.register(Files)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_id', 'file_extension', 'state',  'post_date', 'created_at', )
    list_filter = ('file_name', 'file_id', 'file_extension','state','post_date', 'created_at',)