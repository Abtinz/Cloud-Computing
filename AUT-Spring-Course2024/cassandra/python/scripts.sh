pip install -r requirements.txt

docker pull cassandra

#for test
docker run --rm -d --name cassandra-db  -p 9042:9042 cassandra:latest

docker ps

#docker stop cassandra-db
