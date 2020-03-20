from django.core.exceptions import ValidationError


def validate_nama(value):
    input = value
    if input == "admin":
        message = "maaf, " + value + " tidak boleh daftar"
        raise ValidationError(message)
