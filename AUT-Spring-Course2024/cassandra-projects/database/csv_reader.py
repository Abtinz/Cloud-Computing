import csv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connect to Cassandra
conn_timeout_ms = 4000
auth_provider = PlainTextAuthProvider(username='cassandra', password='password')
cluster = Cluster(['127.0.0.1'], port=9042, connect_timeout=conn_timeout_ms / 1000,auth_provider=auth_provider)
session = cluster.connect('shop')


# Path to your CSV file
file_path = 'AUT-Spring-Course2024\cassandra-projects\database\SampleCSVFile_10600kb.csv'
limitation = 1000
# Open the CSV file and insert data into the table
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if your CSV has one
    for row in reader:
        if limitation > 0:
            if row[8] != '':
                discount = float(row[8])

            else:
                discount = 0.0

            print(row[0], row[1])

            session.execute(
                """
                INSERT INTO sales (product_name, customer_name, quantity, net_sales, unit_price, shipping_cost, region, category, discount)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (row[0], row[1], int(row[2]), float(row[3]), float(row[4]), float(row[5]), row[6], row[7], discount)
            )

            limitation = limitation - 1

print("Data imported successfully.")