#!/usr/bin/python

#This script as used to plot times for running the project scripts (LDSA final project).
#'perf stat -r 10' was used on a bash script that ran Seq_reader.py and Seq_sorter.py.
#The command was issued 7 times, for 1, 5, 10, 15, 20, 60, and 600 copies of 'Small_txt.txt'.
#The result from the run of the whole set, present in 'pdb_seqres.txt', is the last data point

#Have to be before pyplot import
import matplotlib
matplotlib.use('Agg') #Makes it so that plotting doesn't use Xwindows (not possible in VM)

import matplotlib.pyplot as plt

plt.figure().set_size_inches(22, 14.5)

#Plotting is done in regards to copies of 'Small_txt.txt', each of which are 20KB
KB = [20, 100, 200, 200, 400, 1200, 12000, 140000]
Time = [3.8, 3.9, 4.4, 4.1, 4.2, 5.1, 12.7, 67] #Meassurements from 'perf stat'-command, 10 runs

plt.plot(KB, Time)

#Makes everything in the plot pretty
plt.tick_params(labelsize = 20)
plt.title('Average time (10 runs) of scripts working on specific size of data', fontsize = 25, fontweight = 'bold')
plt.xlabel('Data size (KB)', fontsize = 20, fontweight = 'bold')
plt.ylabel('Time (Seconds)', fontsize = 20, fontweight = 'bold')

plt.savefig('Timeplot.png', dpi = 300) #Save plot as figure instead of showing it
