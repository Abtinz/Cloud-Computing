docker cp reducer.py 23605c4878e7:/reducer.py 
docker cp mapper.py 23605c4878e7:/mapper.py  
docker cp input.txt 23605c4878e7:/input.txt

#First SECTION
docker exec -it 23605c4878e7 bin/bash  
hdfs dfs -mkdir -p /user/root/input
hdfs dfs -put /input.txt /user/root/input/input.txt
hadoop jar /opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar     -file mapper.py -mapper mapper.py     -file reducer.py -reducer reducer.py     -input input/input.txt  -output output
hdfs dfs -cat /output/part-00000
cat input.txt | python mapper.py | sort | python reducer.py

#SECOND SECTION

docker cp reducer2.py 23605c4878e7:/reducer2.py 
docker cp mapper2.py 23605c4878e7:/mapper2.py  
docker cp input2.txt 23605c4878e7:/input2.txt
hdfs dfs -put /input2.txt /user/root/input/input2.txt
hadoop jar /opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar     -file mapper2.py -mapper mapper2.py     -file reducer2.py -reducer reducer2.py     -input input/input2.txt  -output output2
hdfs dfs -cat /output2/part-00000
cat input2.txt | python mapper2.py | sort | python reducer2.py

