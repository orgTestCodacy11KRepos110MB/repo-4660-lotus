# Generated by Django 4.0.5 on 2022-09-27 07:15

import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    Subscription = apps.get_model("metering_billing", "Subscription")
    for row in Subscription.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["subscription_uid"])


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0019_subscription_subscription_uid_and_more"),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
