#!/usr/bin/python

#This script as used to plot times for running the project scripts (LDSA final project).
#'perf stat -r 10' was used on a bash script that ran Seq_reader.py and Seq_sorter.py.
#1-5 workers were used, using 1-6 times the size of the dataset 'pdb_seqres.txt'.

#Have to be before pyplot import
import matplotlib
matplotlib.use('Agg') #Makes it so that plotting doesn't use Xwindows (not possible in VM)

import matplotlib.pyplot as plt

plt.figure().set_size_inches(22, 14.5)

#Plotting is done in regards to copies of 'pdb_seqres.txt', each copy is around 140MB
#1-5 workers (thereof the variable names), runtimes as one list, relative data size (1,2,4, and 6 times original) as the other. Runtime rounded of to 4 significant numbers

Data_size = [1, 2, 4, 6]
One = [44.78, 86.84, 168.1, 251.6]
Two = [36.00, 51.17, 112.9, 139.3]
Three = [26.22, 51.17, 78.43, 98.76]
Four =  [29.91, 42.51, 59.57, 83.68] 
Five = [27.09, 38.91, 58.05, 90.74]

plt.plot(Data_size, One)
plt.plot(Data_size, Two)
plt.plot(Data_size, Three)
plt.plot(Data_size, Four)
plt.plot(Data_size, Five)

#Makes everything in the plot pretty
plt.tick_params(labelsize = 20)
plt.title('Average time (10 runs) of scripts working on specific size of data, with 1-5 workers in Spark-cluster', fontsize = 25, fontweight = 'bold')
plt.xlabel('Relative data size (times larger than 140MB)', fontsize = 20, fontweight = 'bold')
plt.ylabel('Time (Seconds)', fontsize = 20, fontweight = 'bold')
lgd = plt.legend(["One", "Two", "Three", "Four", "Five"], bbox_to_anchor=(1.04,1), loc="upper left", fontsize = 20)

plt.savefig('PlotSpark.png', bbox_extra_artists=(lgd,), bbox_inches='tight',  dpi = 300) #Save plot as figure instead of showing it
