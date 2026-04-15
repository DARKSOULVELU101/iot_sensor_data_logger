from datetime import timedelta
from decimal import Decimal
import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from sensors.models import Sensor, SensorReading


class Command(BaseCommand):
    help = 'Create sample IoT sensors and readings for Excel and Power BI analysis.'

    def handle(self, *args, **options):
        SensorReading.objects.all().delete()
        Sensor.objects.all().delete()
        sensor_specs = [
            ('Boiler Room Sensor A', 'multi', 'Boiler Room'),
            ('Cold Storage Sensor B', 'multi', 'Cold Storage'),
            ('Assembly Line Sensor C', 'multi', 'Assembly Line'),
            ('Warehouse Sensor D', 'multi', 'Warehouse'),
            ('Server Room Sensor E', 'multi', 'Server Room'),
        ]
        sensors = []
        for name, sensor_type, location in sensor_specs:
            sensors.append(Sensor.objects.create(name=name, sensor_type=sensor_type, location=location, installation_date=timezone.localdate() - timedelta(days=random.randint(90, 600)), is_active=True))
        now = timezone.now().replace(minute=0, second=0, microsecond=0)
        for hours_back in range(72):
            timestamp = now - timedelta(hours=hours_back)
            for sensor in sensors:
                base_temperature = {'Boiler Room': 38, 'Cold Storage': 4, 'Assembly Line': 27, 'Warehouse': 22, 'Server Room': 19}[sensor.location]
                temperature = Decimal(str(round(base_temperature + random.uniform(-4, 5), 2)))
                humidity = Decimal(str(round(random.uniform(35, 78), 2)))
                pressure = Decimal(str(round(random.uniform(990, 1035), 2)))
                battery_level = Decimal(str(round(max(5, 100 - hours_back * random.uniform(0.04, 0.18) - random.uniform(0, 5)), 2)))
                status = 'normal'
                if temperature > Decimal('42') or battery_level < Decimal('15'):
                    status = 'critical'
                elif temperature > Decimal('35') or humidity > Decimal('70') or battery_level < Decimal('30'):
                    status = 'warning'
                SensorReading.objects.create(sensor=sensor, timestamp=timestamp, temperature=temperature, humidity=humidity, pressure=pressure, battery_level=battery_level, status=status)
        self.stdout.write(self.style.SUCCESS(f'Created {Sensor.objects.count()} sensors and {SensorReading.objects.count()} readings.'))
