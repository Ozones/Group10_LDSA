#Averages time for a script using the terminal


#Installs the needed packages 
#sudo apt install linux-tools-common
#sudo apt install linux-tools-4.4.0-127-generic
#sudo apt install linux-cloud-tools-4.4.0-127-generic

#Performs 10 rounds of the command stated after "-B"
#Outputs to terminal
perf stat -r 10 -B bash Python.sh
