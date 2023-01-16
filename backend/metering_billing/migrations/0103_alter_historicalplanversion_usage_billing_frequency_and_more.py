# Generated by Django 4.0.5 on 2022-12-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "metering_billing",
            "0102_alter_invoicelineitem_associated_subscription_record",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalplanversion",
            name="usage_billing_frequency",
            field=models.CharField(
                blank=True,
                choices=[
                    ("monthly", "Monthly"),
                    ("quarterly", "Quarterly"),
                    ("end_of_period", "End of Period"),
                ],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="planversion",
            name="usage_billing_frequency",
            field=models.CharField(
                blank=True,
                choices=[
                    ("monthly", "Monthly"),
                    ("quarterly", "Quarterly"),
                    ("end_of_period", "End of Period"),
                ],
                max_length=40,
                null=True,
            ),
        ),
    ]
