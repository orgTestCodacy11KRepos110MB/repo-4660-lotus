# Generated by Django 4.0.5 on 2022-12-20 23:06

import uuid

import django.db.models.expressions
from django.db import migrations, models

import metering_billing.utils.utils


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0131_customer_unique_email"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subscriptionrecord",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="backtest",
            name="backtest_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.backtest_uuid,
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.customer_uuid,
                help_text="The id provided when creating the customer, we suggest matching with your internal customer id in your backend",
            ),
        ),
        migrations.AlterField(
            model_name="customerbalanceadjustment",
            name="adjustment_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.customer_balance_adjustment_uuid,
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="historicalbacktest",
            name="backtest_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.backtest_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="historicalcustomer",
            name="customer_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.customer_uuid,
                help_text="The id provided when creating the customer, we suggest matching with your internal customer id in your backend",
            ),
        ),
        migrations.AlterField(
            model_name="historicalmetric",
            name="metric_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.metric_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganization",
            name="organization_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.organization_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganizationsetting",
            name="setting_id",
            field=models.SlugField(default=uuid.uuid4, max_length=100),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="plan_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.plan_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="historicalplanversion",
            name="version_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.plan_version_uuid, max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="historicalproduct",
            name="product_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.product_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubscriptionrecord",
            name="subscription_record_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.subscription_record_uuid,
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubscriptionrecord",
            name="unadjusted_duration_seconds",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="metric",
            name="metric_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.metric_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="oldevent",
            name="idempotency_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.event_uuid,
                help_text="A unique identifier for the specific event being passed in. Passing in a unique id allows Lotus to make sure no double counting occurs. We recommend using a UUID4. You can use the same idempotency_id again after 7 days",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="organization_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.organization_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="organizationinvitetoken",
            name="token",
            field=models.SlugField(default=uuid.uuid4, max_length=250),
        ),
        migrations.AlterField(
            model_name="organizationsetting",
            name="setting_id",
            field=models.SlugField(default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="plan",
            name="plan_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.plan_uuid,
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="planversion",
            name="version_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.plan_version_uuid, max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.product_uuid,
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="subscription_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.subscription_uuid, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="subscriptionrecord",
            name="subscription_record_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.subscription_record_uuid,
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="subscriptionrecord",
            name="unadjusted_duration_seconds",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="webhookendpoint",
            name="webhook_endpoint_id",
            field=models.SlugField(
                default=metering_billing.utils.utils.webhook_endpoint_uuid,
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="webhookendpoint",
            name="webhook_secret",
            field=models.SlugField(
                default=metering_billing.utils.utils.webhook_secret_uuid, max_length=100
            ),
        ),
        migrations.AddConstraint(
            model_name="subscriptionrecord",
            constraint=models.UniqueConstraint(
                fields=("organization", "subscription_record_id"),
                name="unique_subscription_record_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="subscriptionrecord",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("start_date__lte", django.db.models.expressions.F("end_date"))
                ),
                name="end_date_gte_start_date",
            ),
        ),
    ]
