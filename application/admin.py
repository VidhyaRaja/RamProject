from django.contrib import admin
from .models import Site
from .models import Fields

admin.site.register(Site)

class FieldsAdmin(admin.ModelAdmin):
    list_display = ["name", "siteID"]

admin.site.register(Fields, FieldsAdmin)