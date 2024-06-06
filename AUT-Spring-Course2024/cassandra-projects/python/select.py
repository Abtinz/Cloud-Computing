from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

conn_timeout_ms = 4000
auth_provider = PlainTextAuthProvider(username='cassandra', password='password')
cluster = Cluster(['127.0.0.1'], port=9042, connect_timeout=conn_timeout_ms / 1000,auth_provider=auth_provider)
session = cluster.connect('shop')

rows = session.execute("SELECT * FROM sales;" )

for row in rows:
    print(row)

#cluster.shutdown()