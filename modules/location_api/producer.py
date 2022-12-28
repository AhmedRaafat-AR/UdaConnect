import os
from kafka import KafkaProducer
import json 

kafka_server = os.environ["KAFKA_API"]
kafka_topic = os.environ["KAFKA_TOPIC"]

producer = KafkaProducer(bootstrap_servers=kafka_server)
    
def Create(request):
    req = json.dumps(request).encode('utf-8')
    producer.send(kafka_topic, req)
    producer.flush()

    