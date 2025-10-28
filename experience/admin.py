from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'start_date', 'end_date')
    search_fields = ('company', 'role', 'description')
    ordering = ('-start_date',)

