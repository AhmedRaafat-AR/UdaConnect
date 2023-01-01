import os
import json 
from kafka import KafkaConsumer
import modules.location_api.consumer_to_db as to_db


# nodport local
#kafka_server = "localhost:30004"
#kafka_topic = "locations"

# configmap
kafka_server = os.environ["KAFKA_API"]
kafka_topic = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_server)

msg = open(r"msg", "w")

def Read(consumer):
    for location in consumer:
        loc = json.loads(location.value.decode('utf-8'))
        to_db.consumer_to_db(loc)
        print(loc)
        return msg.write(f"{loc}")

Read(consumer)

