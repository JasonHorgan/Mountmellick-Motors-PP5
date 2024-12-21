from django.contrib import admin
from .models import Stock, Reg

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = (
        'reg',
        'make',
        'model',
        'price',
        'description',
        'image',
    )

    ordering = ('reg',)


admin.site.register(Stock, StockAdmin)
admin.site.register(Reg,)

