# Generated by Django 3.2.25 on 2025-02-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0004_alter_order_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="grand_total",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=12
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_total",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=12
            ),
        ),
        migrations.AlterField(
            model_name="orderlineitem",
            name="lineitem_total",
            field=models.DecimalField(
                decimal_places=2, editable=False, max_digits=12
            ),
        ),
    ]
