from django.contrib import admin

from .models import Favor, Agreement


class FavorAdmin(admin.ModelAdmin):
    readonly_fields = ["updated"]
    list_display = ("id", "title", "created", "creator", "doer")


class AgreementAdmin(admin.ModelAdmin):
    readonly_fields = ["updated"]
    list_display = ("id", "user_a_favor", "user_b_favor", "user_a", "user_b")

admin.site.register(Favor, FavorAdmin)
admin.site.register(Agreement, AgreementAdmin)
