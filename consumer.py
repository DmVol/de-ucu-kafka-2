import confluent_kafka
import sys

conf = {'bootstrap.servers': "localhost:9092",
        'group.id': 'mygroup',
        'auto.offset.reset': 'smallest'}

consumer = confluent_kafka.Consumer(conf)

consumer.subscribe(['kafka-test'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == confluent_kafka.KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print('Received message: {}'.format(msg.value().decode('utf-8')))

consumer.close()