from datetime import timedelta
from feast import FeatureView, Field
from feast.types import Float32
from entities import customer
from data_sources import customer_data_source

customer_features = FeatureView(
    name="customer_features",
    entities=[customer],
    ttl=timedelta(days=1),
    schema=[
        Field(name="feature1", dtype=Float32),
        Field(name="feature2", dtype=Float32),
    ],
    online=True,
    source=customer_data_source,
)