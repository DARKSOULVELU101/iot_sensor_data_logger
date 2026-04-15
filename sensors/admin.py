from django.contrib import admin
from .models import Sensor, SensorReading


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sensor_type', 'location', 'installation_date', 'is_active')
    list_filter = ('sensor_type', 'is_active', 'location')
    search_fields = ('name', 'location')


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'timestamp', 'temperature', 'humidity', 'pressure', 'battery_level', 'status')
    list_filter = ('status', 'sensor', 'timestamp')
    search_fields = ('sensor__name', 'sensor__location')
    date_hierarchy = 'timestamp'
