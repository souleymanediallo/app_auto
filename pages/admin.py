from django.contrib import admin
from pages.models import Team


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)