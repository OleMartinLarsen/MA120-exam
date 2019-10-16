hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input Datasets/Posts.xml -output output

