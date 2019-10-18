wordcount = LOAD 'hdfs://localhost/user/root/data' AS (word:chararray, count:int);
wordcount_ordered = order wordcount by $1 DESC;
top10 = LIMIT wordcount_ordered 10;
DUMP top10;