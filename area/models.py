from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=15)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=15)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
