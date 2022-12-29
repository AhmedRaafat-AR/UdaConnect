import os
from kafka import KafkaConsumer
import json 

# nodport local
#kafka_server = "localhost:30004"
#kafka_topic = "locations"

# configmap
# kafka_server = os.environ["KAFKA_API"]
# kafka_topic = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer("locations", bootstrap_servers="localhost:9092")

msg = open(r"msg", "w")

def Read(consumer):
    for location in consumer:
        loc = json.loads(location.value.decode('utf-8'))
        print(loc)
        return msg.write(f"{loc}")

Read(consumer)    