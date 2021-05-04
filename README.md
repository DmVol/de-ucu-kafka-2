# Data streaming - Investigation of kafka throughput
 Home Work 2 for Data Streaming course
 
# Implementation
 - Generator service 
 - Consumer service 
 - Reporting service 
 - MongoDB instance
 - Kafka instance

All the services, except reporting, are implemented as docker containers.

# Setting up
docker-compose up -d --build
For getting monitoring data: python reporter.py

# Managing cluster configuration
Change producers qty: docker-compose scale producer=2
Change consumer qty: docker-compose scale consumer=10
Change partitions qty: docker-compose exec broker kafka-topics --zookeeper zookeeper:2181 --alter --topic kafka-test --partitions 2

# Results
1 Producer, 1 Partition, 1 Consumer

![1_Producer_1_Partitions_1_Consumers](https://user-images.githubusercontent.com/24934034/117033007-aab1f680-ad0a-11eb-8fec-e9c59d5cea0f.png)

1 Producer, 1 Partition, 2 Consumers

![1_Producer_1_Partitions_2_Consumers](https://user-images.githubusercontent.com/24934034/117033009-aab1f680-ad0a-11eb-84c7-3994fd5a4824.png)

1 Producer, 1 Partition, 5 Consumers

![1_Producer_1_Partitions_5_Consumers](https://user-images.githubusercontent.com/24934034/117033013-ab4a8d00-ad0a-11eb-9e80-d3061ad2841d.png)

1 Producer, 1 Partition, 10 Consumers

![1_Producer_1_Partitions_10_Consumers](https://user-images.githubusercontent.com/24934034/117033014-ab4a8d00-ad0a-11eb-8e59-c8e909c56590.png)

1 Producer, 2 Partitions, 2 Consumers

![1_Producer_2_Partitions_2_Consumers](https://user-images.githubusercontent.com/24934034/117033015-abe32380-ad0a-11eb-9ee4-06c35be6ffb6.png)

1 Producer, 2 Partitions, 5 Consumers

![1_Producer_2_Partitions_5_Consumers](https://user-images.githubusercontent.com/24934034/117033016-abe32380-ad0a-11eb-9f94-9819756863b7.png)

1 Producer, 2 Partitions, 10 Consumers

![1_Producer_2_Partitions_10_Consumers](https://user-images.githubusercontent.com/24934034/117033018-abe32380-ad0a-11eb-987b-8274a0886549.png)

1 Producer, 10 Partitions, 10 Consumers

![1_Producer_10_Partitions_10_Consumers](https://user-images.githubusercontent.com/24934034/117033019-ac7bba00-ad0a-11eb-81fe-5cb6a9b4b715.png)

2 Producers, 10 Partitions, 10 Consumers

![2_Producer_10_Partitions_10_Consumers](https://user-images.githubusercontent.com/24934034/117033022-ac7bba00-ad0a-11eb-977c-07290dffbc09.png)
