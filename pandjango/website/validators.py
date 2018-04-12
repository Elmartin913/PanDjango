import re
from django.core.exceptions import ValidationError


def email_validator(value):
    if len(value) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", value) != None:
            raise ValidationError("{} jest bjędny. Wisz poprawny email!".format(value))
    raise ValidationError("{} ma za mało znaków!".format(value))
