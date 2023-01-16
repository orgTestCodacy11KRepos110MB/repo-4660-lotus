# Generated by Django 4.0.5 on 2022-10-25 22:57

from django.db import migrations, models
import metering_billing.utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0051_alter_customer_customer_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="payment_providers",
            new_name="integrations",
        ),
        migrations.RenameField(
            model_name="historicalcustomer",
            old_name="payment_providers",
            new_name="integrations",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="sources",
        ),
        migrations.RemoveField(
            model_name="historicalcustomer",
            name="sources",
        ),
        migrations.AddField(
            model_name="historicalinvoice",
            name="external_payment_obj",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="external_payment_obj",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name="backtest",
            name="time_created",
            field=models.DateTimeField(default=metering_billing.utils.utils.now_utc),
        ),
        migrations.AlterField(
            model_name="historicalbacktest",
            name="time_created",
            field=models.DateTimeField(default=metering_billing.utils.utils.now_utc),
        ),
        migrations.AlterField(
            model_name="historicalinvoice",
            name="external_payment_obj_id",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="historicalinvoice",
            name="issue_date",
            field=models.DateTimeField(
                default=metering_billing.utils.utils.now_utc, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganization",
            name="created",
            field=models.DateField(default=metering_billing.utils.utils.now_utc),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="external_payment_obj_id",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="issue_date",
            field=models.DateTimeField(
                default=metering_billing.utils.utils.now_utc, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="created",
            field=models.DateField(default=metering_billing.utils.utils.now_utc),
        ),
    ]
