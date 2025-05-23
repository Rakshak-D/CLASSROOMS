from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.admin_dashboard_view, name='admin-dashboard'),
    path('upload-timetable/', views.upload_timetable, name='upload-timetable'),
    path('timetable/', views.timetable_management, name='timetable-management'),
    path('bookings/', views.booking_management, name='booking-management'),
    path('events/', views.event_management, name='event-management'),
    path('events/create/', views.event_create_view, name='event-create'),
    path('events/list/', views.event_list_view, name='event-list'),
    path('empty-classrooms/', views.empty_classrooms_view, name='empty-classrooms'),
    path('occupied-classrooms/', views.occupied_classrooms_view, name='occupied-classrooms'),
    path('export-timetable/', views.export_timetable_csv, name='export-timetable'),
    
    # API Routes
    path('api/timetables/', views.all_timetables, name='api-timetables'),
    path('api/timetables/add/', views.add_timetable, name='api-add-timetable'),
    path('api/timetables/update/<int:pk>/', views.update_timetable, name='api-update-timetable'),
    path('api/timetables/delete/<int:pk>/', views.delete_timetable, name='api-delete-timetable'),
    path('api/bookings/', views.BookingListView.as_view(), name='api-bookings'),
    path('api/bookings/<int:pk>/', views.BookingDetailView.as_view(), name='api-booking-detail'),
    path('api/bookings/approve/<int:pk>/', views.approve_booking, name='api-approve-booking'),
    path('api/bookings/reject/<int:pk>/', views.reject_booking, name='api-reject-booking'),
    path('api/events/', views.EventListView.as_view(), name='api-events'),
    path('api/events/create/', views.event_create_api, name='api-event-create'),
    path('api/availability/', views.available_classrooms, name='available-classrooms'),
    path('api/classrooms/', views.classroom_list, name='classroom-list'),
    path('api/teachers/', views.teacher_list, name='teacher-list'),
    path('api/stats/usage/', views.UsageStatsView.as_view(), name='usage-stats'),
    path('api/stats/peakhours/', views.PeakHoursView.as_view(), name='peak-hours'),
    path('api/stats/most-booked/', views.MostBookedClassroomsView.as_view(), name='most-booked-classrooms'),
    path('api/classroom-status/', views.classroom_status, name='classroom-status'),
]
