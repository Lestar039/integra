from django.urls import path
from . import views

urlpatterns = [
    path('', views.analytics, name='analytics_urls'),
    path('ya/', views.start_yandex_analytics, name='start_yandex_analytics')
]
