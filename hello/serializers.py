from rest_framework import serializers
from .models import Mdata

class API_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mdata
        fields = ("published_at", "device_id", "battery", "temp", "pressure")