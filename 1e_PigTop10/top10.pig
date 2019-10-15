lines = LOAD 'data' AS (line:chararray);
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) as word;
grouped = GROUP words BY word;
wordcount = FOREACH grouped GENERATE group, COUNT(words);
wordcount_ordered = order wordcount by $1 DESC;
top10 = LIMIT wordcount_ordered 10;
DUMP top10;