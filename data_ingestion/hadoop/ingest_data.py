from hdfs import InsecureClient

client = InsecureClient('http://localhost:50070', user='user')
local_file = '/path/to/local/file.csv'
hdfs_path = '/path/to/hdfs/file.csv'

client.upload(hdfs_path, local_file)

