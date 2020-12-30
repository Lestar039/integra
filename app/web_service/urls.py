from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_url'),

    path('domains/', views.save_domain, name='domains_urls'),
    path('domain-edit/<str:url_ed>/', views.edit_domain, name='domain_edit_urls'),
    path('domain-delete/<str:url_del>/', views.delete_domain, name='domain_delete_urls'),

    path('hosting/', views.save_hosting, name='hosting_urls'),
    path('hosting-edit/<str:name_ed>/', views.edit_hosting, name='hosting_edit_urls'),
    path('hosting-delete/<str:name_del>/', views.delete_hosting, name='hosting_delete_urls'),

    # services paths
    path('check/', views.start_check, name='check_sites_url'),
]
