from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'], port=9042)
session = cluster.connect('shop')