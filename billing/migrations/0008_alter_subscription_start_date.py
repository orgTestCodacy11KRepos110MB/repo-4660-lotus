# Generated by Django 4.0.6 on 2022-07-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0007_alter_billingplan_billable_metric_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="start_date",
            field=models.DateTimeField(),
        ),
    ]