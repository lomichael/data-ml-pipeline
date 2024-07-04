import os

os.system("hdfs dfs -mkdir -p /user/hadoopuser/input")
os.system("hdfs dfs -chown hadoopuser:hadoopuser /user/hadoopuser/input")
os.system("hdfs dfs -put /path/to/local/datafile /user/hadoopuser/input")

