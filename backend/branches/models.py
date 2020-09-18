from django.db import models


class Branch(models.Model):

    name = models.CharField(max_length=255)
    facade = models.ImageField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Branches'
        permissions = [("hide_coordinates", "Can hide the branch coordinates."), ]

    def to_json(self):
        return {
            "name": self.name,
            "facade": str(self.facade),
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def __str__(self):
        return self.name


class Employee(models.Model):

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
