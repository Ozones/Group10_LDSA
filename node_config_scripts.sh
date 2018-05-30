# Change the permissions of the private key to 0600
sudo chmod 600 ~/.ssh/group10keypair.pem 

#Create a ~/.ssh/config file in order to not to need to type -i [private_key_name] every time
touch ~/.ssh/config
nano ~/.ssh/config
# Add the following to the file
Host 130.238.28.124 #The floating IP address or the host name of the machine.
    IdentityFile ~/.ssh/group10keypair.pem

# SSH:ing to the machine
ssh -L 8888:localhost:8888 -L 8080:localhost:8080 -L 4040:localhost:4040 ubuntu@130.238.28.124 

#////////////Inside the machine///////////////#

# Check what is the hostname and set it
hostname
sudo nano /etc/hosts
# It becomes in this case:
# 127.0.0.1 group101

sudo apt-get update
sudo apt-get upgrade

# Install jdk
sudo apt-get install default-jdk

# Checking that Java is installed correctly
java -version
which java
readlink -f /usr/bin/java

#install pip
sudo apt-get install python3-pip

# Fixing locale not set error
# LC_ALL = (unset)
# perl: warning: Setting locale failed.
echo "export LANGUAGE=en_US.UTF-8 
export LANG=en_US.UTF-8 
export LC_ALL=en_US.UTF-8">>~/.profile
source ~/.profile

# Upgrade pip to the latest version
python3 -m pip install --upgrade pip

# Double check that the version is 10.0.1 
python3 -m pip --version

# Download Spark into home directory
wget http://apache.mirrors.spacedump.net/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz

# Uncompress the Spark file
tar -zxvf spark-2.3.0-bin-hadoop2.7.tgz

# Remove the compressed file
rm spark-2.3.0-bin-hadoop2.7.tgz

# Install jupyter
sudo python3 -m pip install jupyter

# Add these lines to the end of ~/.bashrc
#Spark
export SPARK_HOME="/home/<your_username>/spark-2.3.0-bin-hadoop2.7/"

# Adding environment variables
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre/
export SPARK_HOME=/home/ubuntu/spark-2.3.0-bin-hadoop2.7
export PATH=$PATH:/home/ubuntu/spark-2.3.0-bin-hadoop2.7/bin
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.6-src.zip:$PYTHONPATH
export PATH=$SPARK_HOME/python:$PATH
export PYSPARK_PYTHON=python3">>~/.profile

#update the .profile
source ~/.profile

# Find the master IP 
ifconfig
# In the output, it's the ip address after inet in the second text block

./sbin/start-master.sh -h 127.0.0.1

# When now opening the browser with localhost:8080
# One can see the master URL, in this case it is:
# spark://127.0.0.1:7077 
localhost:8080
# Connect slaves to the master
./sbin/start-slave.sh spark://127.0.0.1:7077 