import confluent_kafka
import sys
import time
import csv

filepath = 'D:/Sources/UCU/Kafka/02-kafka/data/timestamps.csv'

conf = {'bootstrap.servers': "localhost:9092",
        'group.id': 'mygroup',
        'auto.offset.reset': 'smallest'}

consumer = confluent_kafka.Consumer(conf)

consumer.subscribe(['kafka-test'])

while True:
    msg = consumer.poll(1.0)
    # time.sleep(1)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == confluent_kafka.KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([int(time.time() * 1000), msg.timestamp()[1], sys.getsizeof(msg.value())])

    #print(msg.value())

consumer.close()