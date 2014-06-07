from django.core.exceptions import ValidationError


def validate_email_exists(value):
    #Don't do thsi at home! is for avoiding circular dependency
    from profiles.models import User

    """ Raises a Validation error if the user email exists"""
    if User.objects.filter(email=value).exists():
        raise ValidationError("Email already exists")
