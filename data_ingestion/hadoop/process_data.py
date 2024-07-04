from hdfs import InsecureClient

client = InsecureClient('http://localhost:50070', user='hadoopuser')

with client.read('/user/hadoopuser/input/datafile') as reader:
    content = reader.read()
    # Process content

