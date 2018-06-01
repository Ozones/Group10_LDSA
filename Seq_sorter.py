#!/usr/bin/python

from Seq_reader import Lines, sc

AA_dic = ["Charged", "Polar", "Hydrophobic"] #Simplified dictionary           
##AA_dic = ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", 
##"M", "F", "P", "S", "T", "W", "Y", "V"] #Complete (Messier) dictionary
Hash = {key: 0 for key in AA_dic}
max_len = max(Lines, key=len)
Total = []

for i in range(0, len(max_len)):
    Total.append(Hash.copy())

if len(AA_dic) > 3:
    #Following section is only used with complete dictionary
    ######################################################
    for sequence in Lines:
        count = 0

        for letter in sequence:
            if letter in AA_dic:
                Total[count][letter] += 1      
                count += 1
    #######################################################
else:
    #Following section is only used with the simplified dictionary
    ######################################################
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

sc.stop()
