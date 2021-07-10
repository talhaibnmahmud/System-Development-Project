from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex='01[0-9]{9}',
                message='Please provide a valid phone number'
            )
        ]
    )
