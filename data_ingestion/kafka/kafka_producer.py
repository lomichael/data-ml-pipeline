from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_messages(topic, messages):
    for message in messages:
        producer.send(topic, message)
    producer.flush()

if __name__ == "__main__":
    topic = 'data_topic'
    messages = [{"key1": "value1"}, {"key2": "value2"}]  # Example messages
    produce_messages(topic, messages)

