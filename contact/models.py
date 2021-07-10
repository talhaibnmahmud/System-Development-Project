from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=63)
    company = models.CharField(max_length=63, blank=True)
    phone = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex='01[0-9]{9}',
                message='Please provide a valid phone number',
            ),
        ],
        blank=True
    )
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name is not None:
            return self.name
