#!/usr/bin/python

#Have to be before pyplot import
import matplotlib
matplotlib.use('Agg') #Makes it so that plotting doesn't use Xwindows (not possible in VM)

import matplotlib.pyplot as plt

from Testing import Total, AA_dic

plt.figure().set_size_inches(18.5, 10.5)

for i in range(0, len(AA_dic)):
     result = [item[AA_dic[i]] for item in Total]
     plt.plot(result)

#Makes everything in the plot pretty
plt.title('Frequence of occurance for different amino acids at each position in protein sequences', fontsize = 20)
plt.xlabel('Position in sequence', fontsize = 16)
plt.ylabel('Number of occurances of an amino acid', fontsize = 16)
plt.legend(AA_dic, bbox_to_anchor=(1.04,1), loc="upper left")

plt.savefig('Plot.png', dpi = 300) #Save plot as figure instead of showing it
