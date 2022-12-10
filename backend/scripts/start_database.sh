#!/bin/sh

psql -U my_user -d my_database -c "CREATE EXTENSION timescaledb;"
psql -U my_user -d my_database -c "SELECT create_hypertable('metering_billing_', 'time');"


