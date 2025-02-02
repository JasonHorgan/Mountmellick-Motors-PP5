from django.contrib import admin
from .models import FinanceApplication

class FinanceApplicationAdmin(admin.ModelAdmin):
    list_display = ['application_number', 'user', 'car', 'full_name', 'email', 'loan_term', 'application_date']
    search_fields = ['full_name', 'email', 'car__make', 'car__model', 'application_number']
    list_filter = ['loan_term', 'employment_status', 'preferred_contact_method', 'application_date']
    readonly_fields = ['application_number', 'application_date']

admin.site.register(FinanceApplication, FinanceApplicationAdmin)

