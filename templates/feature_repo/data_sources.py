from feast import FileSource
from datetime import datetime

customer_data_source = FileSource(
    path="data/features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)