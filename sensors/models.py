from django.db import models


class Sensor(models.Model):
    SENSOR_TYPES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('pressure', 'Pressure'),
        ('multi', 'Multi Sensor'),
    ]
    name = models.CharField(max_length=120, unique=True)
    sensor_type = models.CharField(max_length=30, choices=SENSOR_TYPES, default='multi')
    location = models.CharField(max_length=160)
    installation_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.location}'


class SensorReading(models.Model):
    STATUS_CHOICES = [('normal', 'Normal'), ('warning', 'Warning'), ('critical', 'Critical')]
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='readings')
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    humidity = models.DecimalField(max_digits=6, decimal_places=2)
    pressure = models.DecimalField(max_digits=7, decimal_places=2)
    battery_level = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='normal')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [models.Index(fields=['timestamp']), models.Index(fields=['status'])]

    def __str__(self):
        return f'{self.sensor.name} at {self.timestamp:%Y-%m-%d %H:%M}'
