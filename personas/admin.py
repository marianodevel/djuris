from django.contrib import admin

from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    model = Persona


admin.site.register(Persona)
