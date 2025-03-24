from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            'id',
            'name',
            'latitude',
            'longitude',
            'elevation',
            'created_at'
        ]



    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Location name cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Location name must be at least 3 characters long.")
        return value