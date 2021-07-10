from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

from area.models import District, Division


# Create your models here.
class House(models.Model):
    CATEGORY = (
        ('Apartment', 'Apartment'),
        ('Duplex', 'Duplex'),
        ('Triplex', 'Triplex'),
        ('Sublet', 'Sublet'),
    )

    title = models.CharField(max_length=127)
    address = models.CharField(max_length=127)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    category = models.CharField(max_length=15, choices=CATEGORY, default=CATEGORY[0][0])
    price = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(1000000)])
    area = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(100000)])
    beds = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(15)])
    baths = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    kitchen = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    drawing = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    dining = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    parking_space = models.PositiveSmallIntegerField(default=0, blank=True)
    elevators = models.PositiveSmallIntegerField(default=0, blank=True)

    balcony = models.BooleanField(default=False)
    electricity_backup = models.BooleanField(default=False)
    service_elevator = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        if self.title is not None:
            return str(self.title)


def user_directory_path(instance, filename):
    return f'uploads/%Y/%m/%d/user_{instance.house.owner.id}/{filename}'


class Photo(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo for - {self.house.title}'


# TODO: Add list editable to False
class Favourite(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('house', 'user')

    def __str__(self):
        return f'{self.user.username} loves {self.house.title}'
