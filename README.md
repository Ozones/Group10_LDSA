# Group10_LDSA
LDSA project: Count occurance of different amino acids at each position in proteins, generalize this and visualize it
This Github-repository is part of the final project in the course 'Large datasets for scientific applications, 10c', Uppsala University, spring of 2018. 
Authors of this repository is Simon Ekdahl, Swathi Kamani, and Lauri Mesilaakso.

This repository contains bash-scripts for implementing Spark-clusters (Apache). It was made for 
clusters created on the SNIC Science Cloud platform. 

Scripts to read sequence-files of proteins from the Protein Data Bank, count the occurance of each type of amino acid on each position for every sequence, and then visualize these, was the goal of this project. Since large datasets would require a distributed solution, this was done using Spark-clusters.

'Seq_reader.py' reads in a folder containing sequence files. These files has to have a header for each new sequence, and the
next line being the whole sequence in question for this script to work. Each sequence can either be in one file, or as one file per sequence. 

'Seq_sorter.py' Takes all the seqences and parses them. A list of dictionaries is created where the keys are each type of amino acid, and the values are counters for the number of times that the amino acid occurs at that specific position in the list (a sequence). This list of dictionaries is as long as the longest sequence that has been read, so that all positions can be represented.

'Plot.py' takes the list of dictionaries and plots each type of amino acid as one curve on a graph, creating several curves on one figure.

Since all the above mentioned scripts are dependant on eachother, the have to be run in sequence. So the 'Seq_reader.py' have to run first, followed by 'Seq_sorter.py', followed by 'Plot.py' (if you want the results visualized). 

'Seq_reader.py' have to be followed by 'Seq_sorter.py'. Running the first script twice without 'Seq_sorter.py' will result in an error. 

The scripts 'TimerplotLocal.py' and 'TimerplotSpark.py' graphs runtimes for the above scripts, and was used for creating graphs for the final report, and have all variables hard-coded into them. 

'Timer.sh' and 'Python.sh' was used to meassure runtime of the scripts.
