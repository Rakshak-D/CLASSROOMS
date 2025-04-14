from django.contrib import admin
from django.utils.html import format_html
from timetable.models import Timetable
from classroom.models import Classroom
from booking.models import Booking

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('day', 'formatted_time', 'classroom', 'teacher')
    list_filter = ('day', 'classroom__block', 'teacher')
    search_fields = ('day', 'classroom__name', 'teacher__username')
    autocomplete_fields = ['classroom', 'teacher']
    ordering = ('day', 'start_time')
    list_per_page = 50

    def formatted_time(self, obj):
        return f"{obj.start_time.strftime('%H:%M')} - {obj.end_time.strftime('%H:%M')}"
    formatted_time.short_description = 'Time Slot'

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'block', 'capacity', 'status', 'status_badge')  # Added 'status' to list_display
    list_filter = ('block', 'status')
    search_fields = ('name', 'block')
    list_editable = ('status',)
    list_per_page = 50

    def status_badge(self, obj):
        color = 'green' if obj.status == 'free' else 'red'
        return format_html(
            '<span style="color: white; background-color: {}; padding: 2px 8px; border-radius: 4px">{}</span>',
            color,
            'Available' if obj.status == 'free' else 'Occupied'
        )
    status_badge.short_description = 'Status'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'classroom', 'formatted_date', 'time_slot', 'status_badge')
    list_filter = ('status', 'date', 'classroom__block')
    search_fields = ('user__username', 'classroom__name')
    raw_id_fields = ('user', 'classroom')
    date_hierarchy = 'date'
    ordering = ('-date', 'start_time')
    actions = ['approve_selected', 'reject_selected']
    list_per_page = 50

    def formatted_date(self, obj):
        return obj.date.strftime("%b %d, %Y")
    formatted_date.admin_order_field = 'date'
    formatted_date.short_description = 'Date'

    def time_slot(self, obj):
        return f"{obj.start_time.strftime('%H:%M')} - {obj.end_time.strftime('%H:%M')}"
    time_slot.short_description = 'Time Slot'
    
    def status_badge(self, obj):
        colors = {
            'pending': 'orange',
            'approved': 'green',
            'rejected': 'red'
        }
        return format_html(
            '<span style="color: white; background-color: {}; padding: 2px 8px; border-radius: 4px">{}</span>',
            colors[obj.status],
            obj.status.capitalize()
        )
    status_badge.short_description = 'Status'
    
    @admin.action(description='Approve selected bookings')
    def approve_selected(self, request, queryset):
        queryset.update(status='approved')
    
    @admin.action(description='Reject selected bookings')
    def reject_selected(self, request, queryset):
        queryset.update(status='rejected')

