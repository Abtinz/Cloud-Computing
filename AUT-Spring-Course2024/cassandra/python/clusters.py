from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

conn_timeout_ms = 4000
auth_provider = PlainTextAuthProvider(username='cassandra', password='password')
cluster = Cluster(['127.0.0.1'], port=9042, connect_timeout=conn_timeout_ms / 1000,auth_provider=auth_provider)
session = cluster.connect()

metadata = cluster.metadata
print("Cluster Name:", metadata.cluster_name)

print("\nKeyspaces:")
for keyspace in metadata.keyspaces:
    print(keyspace)

print("\nNodes in the cluster:")
for host in metadata.all_hosts():
    print(f"Host: {host.address}, Rack: {host.rack}, Datacenter: {host.datacenter}")