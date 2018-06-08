#!/usr/bin/python

import findspark
findspark.init('/home/ozones/spark-2.3.0-bin-hadoop2.7')
import pyspark

sc = pyspark.SparkContext(appName="Read")

file = sc.textFile('/home/ozones/LDSA/Seqs/')
llist = file.collect()

# print the list
count = 0  
Lines = []

for line in llist:
    count += 1
    if count % 2 == 0:
        Lines.append(line)
