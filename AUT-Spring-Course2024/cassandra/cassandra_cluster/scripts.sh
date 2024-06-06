pip install -r requirements.txt

docker pull cassandra

#for test
docker run --rm -d --name cassandra-db  -p 9042:9042 cassandra:latest

docker ps

docker stop cassandra-db

#lets fire the clusters
cd cassandra_cluster
docker compose up -d
docker ps
#cluster niformation
docker exec -it firt-cassandra-service nodetool info
docker exec -it second-cassandra-service nodetool info
docker exec -it third-cassandra-service nodetool info

docker-compose down