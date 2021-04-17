import confluent_kafka
import socket

file = 'D:/Sources/UCU/Kafka/02-kafka/data/reddit_dataset.csv'
conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = confluent_kafka.Producer(conf)

with open(file, "rb") as csvfile:
    reader = csvfile.readlines()
    for row in reader:
        producer.produce(topic="kafka-test", value=row)
        producer.flush()

#chunks = pd.read_csv(file, delimiter=",", chunksize=100000)
#i = 0
#for chunk in chunks:
#    for row in chunk.values:
#        data = str(row)
#        producer.produce(topic="kafka-test",  value=data.encode())
#        producer.flush()
#        #print(list(row))
#        #i += 1
#        #if i > 1:
#        #    break