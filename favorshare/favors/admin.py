from django.contrib import admin

from .models import Favor


class FavorAdmin(admin.ModelAdmin):
    readonly_fields = ["updated"]
    list_display = ("id", "title", "created", "creator", "doer")


admin.site.register(Favor, FavorAdmin)
