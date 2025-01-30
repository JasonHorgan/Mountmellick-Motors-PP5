from django.db import models
from django.core.validators import RegexValidator

class Stock(models.Model):
    reg_number = models.CharField(
        max_length=254,
        unique=True,
        validators=[RegexValidator(regex='^[A-Za-z0-9]*$', message='Registration number must be alphanumeric')]
    )
    make = models.CharField(max_length=254, null=True, blank=True)
    model = models.CharField(max_length=254, null=True, blank=True)
    fuel_type = models.CharField(max_length=254, null=True, blank=True)
    transmission_type = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.make
