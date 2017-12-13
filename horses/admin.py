from django.contrib import admin

from .models import Horse


class HorseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Horse, HorseAdmin)
