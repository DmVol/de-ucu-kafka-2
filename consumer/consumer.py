import confluent_kafka
import sys
import time
import pymongo
import uuid

process_uuid = uuid.uuid1().hex[:8]

# Add sleep while worker is starting
time.sleep(10)

client = pymongo.MongoClient('mongo', 27017)
db = client.stream_benchmark
data = db.data

conf = {'bootstrap.servers': "broker:29092",
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
    print(time.time())
    row = {"process": process_uuid, "consumer_ts": int(time.time() * 1000), "kafka_ts": msg.timestamp()[1], "msg_size": sys.getsizeof(msg.value())}

    data.insert_one(row)

consumer.close()