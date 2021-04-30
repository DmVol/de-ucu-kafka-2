import confluent_kafka
import socket
import csv
import json
import time

filepath = 'reddit_dataset.csv'

conf = {'bootstrap.servers': "broker:29092",
        'client.id': socket.gethostname()}

producer = confluent_kafka.Producer(conf)

with open(filepath, encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        producer.poll(0)
        row['producer_timestamp'] = int(time.time() * 1000)
        json_data = json.dumps(row).encode('utf-8')
        producer.produce(topic="kafka-test", value=json_data)

producer.flush()
