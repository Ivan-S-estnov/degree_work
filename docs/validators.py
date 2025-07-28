from rest_framework.serializers import ValidationError

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

def validate_forbidden_words(value):
    if value.lower() in forbidden_words:
        raise ValidationError["Использовано запрещенное слово"]
