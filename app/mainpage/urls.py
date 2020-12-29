from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index_page, name='index_urls'),
    # path('', IndexPageView.as_view(), name='index_urls'),
    path('analytics/', AnalyticsView.as_view(), name='analytics_urls'),
    path('calendar/', CalendarView.as_view(), name='calendar_urls'),
]
