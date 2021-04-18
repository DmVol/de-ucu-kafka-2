import confluent_kafka
import socket
import csv
import json
import sys

filepath = 'D:/Sources/UCU/Kafka/02-kafka/data/top.csv'
conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = confluent_kafka.Producer(conf)

with open(filepath, encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        json_data = json.dumps(row).encode('utf-8')
        print(sys.getsizeof(json_data))
        producer.produce(topic="kafka-test", value=json_data)
        producer.flush()