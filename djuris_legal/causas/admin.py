from django.contrib import admin

from .models import Causa


class CausaAdmin(admin.ModelAdmin):
    model = Causa


admin.site.register(Causa)
