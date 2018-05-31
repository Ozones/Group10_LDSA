#!/usr/bin/python

#Have to be before pyplot import
import matplotlib
matplotlib.use('Agg') #Makes it so that plotting doesn't use Xwindows (not possible in VM)

import matplotlib.pyplot as plt

from Testing import Total, AA_dic

for i in range(0, len(AA_dic)):
     result = [item[AA_dic[i]] for item in Total]
     plt.plot(result)

plt.legend(AA_dic)
plt.savefig('Plot.png') #Save plot as figure instead of showing it
