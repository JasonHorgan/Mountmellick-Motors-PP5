from django.db import models

# Create your models here.

class Reg(models.Model):

    class Meta:
        verbose_name_plural = 'Registration numbers'

    reg_number = models.CharField(max_length=254)

    def __str__(self):
        return self.reg_number


class Stock(models.Model):
    reg = models.ForeignKey('Reg', null=True, blank=True, on_delete=models.SET_NULL)
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