from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard_urls'),

    path('domain/<int:pk>/', views.save_domain, name='domains_urls'),
    path('domain-edit/<int:pk>/<str:url_ed>/', views.edit_domain, name='domain_edit_urls'),
    path('domain-delete/<int:pk>/<str:url_del>/', views.delete_domain, name='domain_delete_urls'),

    path('hosting/<int:pk>/', views.save_hosting, name='hosting_urls'),
    path('hosting-edit/<int:pk>/<str:name_ed>/', views.edit_hosting, name='hosting_edit_urls'),
    path('hosting-delete/<int:pk>/<str:name_del>/', views.delete_hosting, name='hosting_delete_urls'),

    # services paths
    path('check/', views.start_check, name='check_sites_urls'),
    path('user-redirect', views.redirect_to_user_page, name='redirect_to_user_page'),
]
