# Generated by Django 4.0.5 on 2022-11-01 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0059_alter_historicalinvoice_invoice_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="name",
            new_name="customer_name",
        ),
        migrations.RenameField(
            model_name="historicalcustomer",
            old_name="name",
            new_name="customer_name",
        ),
    ]
