import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_sensor_data_logger.settings')
application = get_wsgi_application()
