from django.contrib import admin
from .models import TestDrive


class TestDriveAdmin(admin.ModelAdmin):
    list_display = ["user", "car", "date", "time", "status", "created_at"]
    search_fields = ["user__username", "car__make", "car__model"]
    list_filter = ["status", "date"]
    readonly_fields = ["created_at"]


admin.site.register(TestDrive, TestDriveAdmin)
