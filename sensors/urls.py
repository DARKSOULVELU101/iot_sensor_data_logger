from django.urls import path
from . import views

app_name = 'sensors'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sensors/', views.sensor_list, name='sensor_list'),
    path('sensors/add/', views.sensor_create, name='sensor_create'),
    path('sensors/<int:pk>/edit/', views.sensor_update, name='sensor_update'),
    path('readings/', views.reading_list, name='reading_list'),
    path('readings/add/', views.reading_create, name='reading_create'),
    path('readings/<int:pk>/delete/', views.reading_delete, name='reading_delete'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('api/dashboard-data/', views.dashboard_data, name='dashboard_data'),
]
