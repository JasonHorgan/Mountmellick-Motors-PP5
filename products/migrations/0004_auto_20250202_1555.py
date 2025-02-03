# Generated by Django 3.2.25 on 2025-02-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_auto_20250130_1518"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="fuel_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("petrol", "Petrol"),
                    ("diesel", "Diesel"),
                    ("electric", "Electric"),
                    ("hybrid", "Hybrid"),
                    ("other", "Other"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="transmission_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("manual", "Manual"),
                    ("automatic", "Automatic"),
                    ("semi_automatic", "Semi-Automatic"),
                    ("other", "Other"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
