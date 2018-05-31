#!/usr/bin/python

#Have to be before pyplot import
import matplotlib
matplotlib.use('Agg') #Makes it so that plotting doesn't use Xwindows (not possible in VM)

import matplotlib.pyplot as plt

Lines = []
with open('Small_txt.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0: #this is the remainder operator
           Lines.append(line)

AA_dic = ["Charged", "Polar", "Hydrophobic"]           
##AA_dic = ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", 
##"M", "F", "P", "S", "T", "W", "Y", "V"]
Hash = {key: 0 for key in AA_dic}
max_len = max(Lines, key=len)
Total = []

for i in range(0, len(max_len)):
    Total.append(Hash.copy())

for sequence in Lines:
    count = 0
    for letter in sequence:
        if letter in ('R', 'K', 'D', 'E'):
            Total[count]["Charged"] += 1
            count += 1
        if letter in ('Q', 'N', 'H', 'S', 'T', 'Y', 'C', 'W'):
            Total[count]["Polar"] += 1
            count += 1
        if letter in ('A', 'I', 'L', 'M', 'F', 'V', 'P', 'G'):
            Total[count]["Hydrophobic"] += 1
            count += 1


##for sequence in Lines:
##    count = 0
##    for letter in sequence:
##        if letter in AA_dic:
##            Total[count][letter] += 1
##            count += 1

for i in range(0, len(AA_dic)):
    result = [item[AA_dic[i]] for item in Total]
    plt.plot(result)
    plt.legend()

plt.savefig('Plot.png') #Save plot as figure instead of showing it
