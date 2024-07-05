from kafka import KafkaConsumer
from hdfs import InsecureClient
import json

consumer = KafkaConsumer('test-topic', bootstrap_servers=['localhost:9092'])
hdfs_client = InsecureClient('http://localhost:9870', user='hadoopuser')

try:
    with hdfs_client.write('/data/kafka_data.json', encoding='utf-8', append=True) as writer:
        for message in consumer:
            writer.write(json.dumps(message.value.decode('utf-8')) + '\n')
except hdfs.util.HdfsError:
    hdfs_client.write('/data/kafka_data.json', encoding='utf-8')  # Create the file if it doesn't exist
    with hdfs_client.write('/data/kafka_data.json', encoding='utf-8', append=True) as writer:
        for message in consumer:
            writer.write(json.dumps(message.value.decode('utf-8')) + '\n')

