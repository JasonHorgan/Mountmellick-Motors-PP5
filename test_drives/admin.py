from django.contrib import admin
from .models import TestDrive

@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'car__make', 'car__model')
