import uuid
from django.db import models
from django.contrib.auth.models import User
from products.models import Stock

class FinanceApplication(models.Model):
    application_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Stock, on_delete=models.CASCADE)  
    application_date = models.DateTimeField(auto_now_add=True)
    

    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    employment_status = models.CharField(max_length=50, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')])
    monthly_income = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0)
    loan_term = models.IntegerField(choices=[(12, '12 months'), (24, '24 months'), (36, '36 months'), (48, '48 months')])
    preferred_contact_method = models.CharField(max_length=50, choices=[('Email', 'Email'), ('Phone', 'Phone')])
    
    def _generate_order_number(self):
        """
        Generate a random, unique application number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.application_number:
            self.application_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Finance Application for {self.car.make} {self.car.model} by {self.user.username}"
