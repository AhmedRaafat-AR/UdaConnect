import os
from kafka import KafkaConsumer
import json 

# nodport
kafka_server = "localhost:30004"
kafka_topic = "locations"

# configmap
# kafka_server = os.environ["Kafka_API"]
# kafka_topic = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_server)

def Read(consumer):
    for location in consumer:
        loc = json.loads(location.value.decode('utf-8'))
        print (loc)

Read(consumer)    