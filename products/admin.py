from django.contrib import admin
from .models import Stock

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = (
        'make',
        'model',
        'price',
        'description',
        'image',
    )

    ordering = ('make',)


admin.site.register(Stock, StockAdmin)

