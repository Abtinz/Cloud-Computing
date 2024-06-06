pip install -r requirements.txt

docker pull cassandra

#for test
docker run --rm -d --name cassandra-shop  -p 9042:9042 cassandra:latest

docker ps

docker exec -it cassandra-shop nodetool info

#docker stop cassandra-db
