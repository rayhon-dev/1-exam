from rest_framework.exceptions import ValidationError


def validate_temperature(value):
    if value < -100 or value > 100:
        raise ValidationError("Temperature must be between -100 and 100 degrees.")

def validate_humidity(value):
    if value < 0 or value > 100:
        raise ValidationError("Humidity must be between 0 and 100 percent.")
