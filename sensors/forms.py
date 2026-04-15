from django import forms
from .models import Sensor, SensorReading


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'sensor_type', 'location', 'installation_date', 'is_active']
        widgets = {'installation_date': forms.DateInput(attrs={'type': 'date'})}


class SensorReadingForm(forms.ModelForm):
    class Meta:
        model = SensorReading
        fields = ['sensor', 'timestamp', 'temperature', 'humidity', 'pressure', 'battery_level', 'status', 'notes']
        widgets = {'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}), 'notes': forms.Textarea(attrs={'rows': 3})}


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='CSV file')
