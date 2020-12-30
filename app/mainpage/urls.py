from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.save_url, name='save_urls'),
    path('delete-url/<str:url_del>/', views.delete_url, name='delete_urls'),

    # services paths
    path('check/', views.start_check, name='check_sites_url'),
    path('time/', views.time, name='time_url'),

    path('analytics/', AnalyticsView.as_view(), name='analytics_urls'),
    path('calendar/', CalendarView.as_view(), name='calendar_urls'),
]
