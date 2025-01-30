import pyspark 
import sys

BUCKET = "test-gcs-418919"
inputUri=f"gs://{BUCKET}/test.txt" 
outputUri=f"gs://{BUCKET}/test_file_output"
sc = pyspark.SparkContext()
lines = sc.textFile(inputUri)
words = lines.flatMap(lambda line: line.split())
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda count1 , count2: counti + count2) 
wordCounts.saveAsTextFile(outputUri)
