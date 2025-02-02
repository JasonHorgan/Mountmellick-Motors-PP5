from django.db import models
from django.core.validators import RegexValidator

class Stock(models.Model):
    # Choices for fuel type and transmission type
    FUEL_TYPE_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
        ('other', 'Other'),
    ]
    
    TRANSMISSION_TYPE_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('semi_automatic', 'Semi-Automatic'),
        ('other', 'Other'),
    ]

    reg_number = models.CharField(
        max_length=254,
        unique=True,
        validators=[RegexValidator(regex='^[A-Za-z0-9]*$', message='Registration number must be alphanumeric')]
    )
    make = models.CharField(max_length=254, null=True, blank=True)
    model = models.CharField(max_length=254, null=True, blank=True)
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPE_CHOICES,
        null=True,
        blank=True
    )
    transmission_type = models.CharField(
        max_length=20,
        choices=TRANSMISSION_TYPE_CHOICES,
        null=True,
        blank=True
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.make
