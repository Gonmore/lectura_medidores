from django import forms
from . models import Meter

class MeterForm(forms.ModelForm):
    class Meta:
        model = Meter
        fields = [
            'name',
            'serial',
            'logical_name',
            'model',
            'location',
            'group',
            'con_method',
            'con_port',
            'con_ip',
            'baud_rate',
        ]