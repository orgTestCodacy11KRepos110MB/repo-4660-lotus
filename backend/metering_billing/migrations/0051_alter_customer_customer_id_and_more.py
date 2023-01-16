# Generated by Django 4.0.5 on 2022-10-25 00:06

from django.db import migrations, models
import metering_billing.utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0050_historicalplan_historicalplanversion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="customer_id",
            field=models.CharField(
                blank=True,
                default=metering_billing.utils.utils.customer_uuid,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcustomer",
            name="customer_id",
            field=models.CharField(
                blank=True,
                default=metering_billing.utils.utils.customer_uuid,
                max_length=50,
            ),
        ),
    ]
