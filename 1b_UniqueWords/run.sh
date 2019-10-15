# Assumptions:
# 1. the dataset in the cluster is located at "news"
# 2. the current directory contains files mapper.py and reducer.py for mapper and reducer code respectively

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input news -output out
