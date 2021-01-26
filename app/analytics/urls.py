from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.analytics, name='analytics_urls'),
    path('ya/<str:pk>/', views.start_yandex_analytics, name='start_yandex_analytics')
]
