from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connect to Cassandra:9042
conn_timeout_ms = 4000
auth_provider = PlainTextAuthProvider(username='cassandra', password='password')
cluster = Cluster(['127.0.0.1'], port=9042, connect_timeout=conn_timeout_ms / 1000,auth_provider=auth_provider)
session = cluster.connect('shop')

session.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product_name text,
    customer_name text,
    quantity int,
    net_sales float,
    unit_price float,
    shipping_cost float,
    region text,
    category text,
    discount float,
    PRIMARY KEY (product_name, customer_name)
);
""")

print("sales table is created successfully ...")