from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'data_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_serializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    print(message.value)

