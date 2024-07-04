from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {'value': 'test_data'}
    producer.send('test', value=data)
    time.sleep(1)

