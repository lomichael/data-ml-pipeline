from kafka import KafkaConsumer
import json
from hdfs import InsecureClient
import redis

consumer = KafkaConsumer(
    'test',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

hdfs_client = InsecureClient('http://localhost:50070', user='hadoopuser')
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

for message in consumer:
    data = message.value
    with hdfs_client.write('/data/kafka_data.json', encoding='utf-8', append=True) as writer:
        writer.write(json.dumps(data) + '\n')
    redis_client.set('latest_data', json.dumps(data))

