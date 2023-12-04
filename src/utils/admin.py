from django.contrib import admin
from . import models

admin.site.register(models.Region)
admin.site.register(models.District)
admin.site.register(models.State)
admin.site.register(models.Language)
admin.site.register(models.Category)
admin.site.register(models.Specialization)