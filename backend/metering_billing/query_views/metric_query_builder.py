import psycopg3
from settings import DATABASES
from metering_billing.models import Metric
import configparser


class QUERY_BUILDER_NAME:
    COUNTER_SUM = "counter_sum"
    COUNTER_COUNT = "counter_count"
    COUNTER_UNIQUE = "counter_unique"
    COUNTER_MAX = "counter_max"
    CONTINUOUS_MAX = "continuous_max"


class QUERY_BUCKET_SIZE:
    COUNTER = ("1 day", "day")
    CONTINUOUS = ("1 hour", "hour")


# Get database connection settings
DATABASE_SETTINGS = settings["default"]


def run_query(query_name, file_name, *args):

    # Read the queries.properties file
    config = configparser.ConfigParser()
    config.read(file_name)

    policy_config = configparser.ConfigParser()
    policy_config.read("file_name")

    # Get the SQL query from the file
    sql = config[query_name]

    # Connect to the database
    conn = psycopg3.connect(
        "host=localhost dbname=my_database user=my_user password=my_password"
    )
    cur = conn.cursor()

    # Execute the Create View SQL query with the supplied arguments
    cur.execute(sql, args)

    cur.execute()
    conn.commit()


# Each one of these we have to input the metric name and the interval in how many days back we look at as well as the property to look at


def create_view(metric: Metric, interval, property):

    metric_type = metric.metric_type
    metric_aggregation = metric.usage_aggregation_type
    metric_id = metric.metric_id
    metric_property = metric.billable_metric_property
    file_name = "materialized_view.properties"

    if metric_type == "counter":

        if metric_aggregation == "sum":
            query_name = QUERY_BUILDER_NAME.COUNTER_SUM
            run_query(query_name, file_name, metric_id)

        else:
            if metric_aggregation == "count":
                query_name = QUERY_BUILDER_NAME.COUNTER_COUNT
            elif metric_aggregation == "unique":
                query_name = QUERY_BUILDER_NAME.COUNTER_UNIQUE
            elif metric_aggregation == "max":
                query_name = QUERY_BUILDER_NAME.COUNTER_MAX

            run_query(query_name, file_name, metric_id, metric_property)

    # elif metric_type == "continuous":

    #     if metric_aggregation == "max":
    #         query_name = QUERY_BUILDER_NAME.CONTINUOUS_MAX

    #     run_query(query_name, metric_name, property)


### Delete view when metric is deleted and no longer a part of any plans
def delete_view(metric: Metric):
    metric_id = metric.metric_id
    file_name = "delete_views.properties"

    run_query("counter_count", file_name, metric_id)
