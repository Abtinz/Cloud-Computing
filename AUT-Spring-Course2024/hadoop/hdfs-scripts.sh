docker cp reducer.py 23605c4878e7:/reducer.py 
docker cp mapper.py 23605c4878e7:/mapper.py  
docker cp input.txt 23605c4878e7:/input.txt


docker exec -it 23605c4878e7 bin/bash  
hdfs dfs -mkdir -p /user/root/input
hdfs dfs -put /input.txt /user/root/input/input.txt
hadoop jar /opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar     -file mapper.py -mapper mapper.py     -file reducer.py -reducer reducer.py     -input input/input.txt 
-output output

cat input.txt | python mapper.py | sort | python reducer.py