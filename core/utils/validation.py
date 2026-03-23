import bleach
import re

class Validation:
    @staticmethod
    def sanitize(text):
        if not text: return text
        return bleach.clean(text)

    @staticmethod
    def is_email(text):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, text) is not None

    @staticmethod
    def required(data, fields):
        missing = []
        for field in fields:
            if field not in data or not data[field]:
                missing.append(field)
        return missing

    @staticmethod
    def validate(data, rules):
        # Very simple rule validation demo
        errors = {}
        for field, rule_str in rules.items():
            value = data.get(field)
            if 'required' in rule_str and not value:
                errors[field] = "Field is required"
            elif 'email' in rule_str and value and not Validation.is_email(value):
                errors[field] = "Invalid email format"
        return errors
