pip install -r requirements.txt

docker pull cassandra

#for test
docker run --rm -d --name cassandra-db cassandra:latest

docker ps

docker stop cassandra-db

#lets fire the clusters
docker compose up -d
docker ps
docker exec -it firt-cassandra-service nodetool info
docker exec -it second-cassandra-service nodetool info
docker exec -it third-cassandra-service nodetool info

docker dpwn up -d
