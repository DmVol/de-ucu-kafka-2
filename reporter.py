import time
import pymongo
from matplotlib import pyplot as plt


def get_attribute(cursor, attribute):
    value = None
    for row in cursor:
        value = row[attribute]
        if value is not None:
            break
    return value


def initialize_mongo(port):
    mongo_connection = pymongo.MongoClient('localhost', port)
    database = mongo_connection.stream_benchmark
    return database.data


if __name__ == "__main__":
    runs = 0

    max_deltas = []
    throughput_measures = []

    table = initialize_mongo(port=27017)

    while runs < 60:

        last_row = table.find_one(sort=[('_id', pymongo.DESCENDING)])
        first_row = table.find_one(sort=[('_id', pymongo.ASCENDING)])
        sum_agg = table.aggregate([{'$group': {'_id': 1, 'all': {'$sum': '$msg_size'}}}])

        timing = (last_row['consumer_ts'] - first_row['producer_ts']) / 1000
        data_size = get_attribute(sum_agg, 'all')

        get_max_diff = table.aggregate(
        [{'$group': {'_id': 1, "diff": {'$max': {'$abs': {'$subtract': ['$consumer_ts', "$producer_ts"]}}}}}])

        max_diff = get_attribute(get_max_diff, 'diff') / 1000

        throughput = (data_size / timing / (1024 * 1024)) * 8

        max_deltas.append(max_diff)
        throughput_measures.append(throughput)

        runs += 1

        time.sleep(1)

    measures = list(range(1, runs + 1))
    plt.subplot(2, 1, 1)
    plt.plot(measures, throughput_measures)
    plt.title('Kafka metrics')
    plt.ylabel('Mb/s')

    plt.subplot(2, 1, 2)
    plt.plot(measures, max_deltas)
    plt.plot(max_deltas)
    plt.xlabel('Timeline (seconds)')
    plt.ylabel('Max message delay (seconds)')

    plt.show()

    command = input("Do you want to clear the statistics? (y/n): ")
    if command == "y":
        table.delete_many({})
