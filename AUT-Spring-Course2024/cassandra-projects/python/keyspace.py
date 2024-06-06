from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

conn_timeout_ms = 4000
auth_provider = PlainTextAuthProvider(username='cassandra', password='password')
cluster = Cluster(['127.0.0.1'], port=9042, connect_timeout=conn_timeout_ms / 1000,auth_provider=auth_provider)
session = cluster.connect('shop')

create_keyspace_query = """
CREATE KEYSPACE IF NOT EXISTS shop
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': '3' 
};
"""

session.execute(create_keyspace_query)
print("Keyspace 'shop' created successfully.")


session = cluster.connect('shop')
