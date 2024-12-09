from rest_framework import serializers
from .models import Meter, Con_method,Model,Vendor

class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = '__all__'

class ConMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Con_method
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'