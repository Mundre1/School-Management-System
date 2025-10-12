from django.contrib import admin
from .models import Event, Holiday


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_date', 'end_date', 'location', 'is_public']
    list_filter = ['event_type', 'is_public', 'start_date']
    search_fields = ['title', 'description', 'location']
    ordering = ['start_date']


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'is_recurring']
    list_filter = ['is_recurring', 'date']
    search_fields = ['name', 'description']
    ordering = ['date']
