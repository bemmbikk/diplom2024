import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    pattern = re.compile(r'^(\+7|8)\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$')
    if not pattern.match(value):
        raise ValidationError(('Номер телефона должен начинаться с +7 или 8'),
            code='invalid_phone_number',
            params={'value': value},
        )
