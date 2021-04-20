import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.stream_benchmark
data = db.data

last_row = data.find_one(sort=[( '_id', pymongo.DESCENDING)])
first_row = data.find_one(sort=[( '_id', pymongo.ASCENDING)])
sum_agg = data.aggregate([{'$group': {'_id': 1, 'all': { '$sum': '$msg_size' } } } ])

data_size = 0

for r in sum_agg:
    data_size = r['all']
    if data_size is not None:
        break

timing = (last_row['consumer_ts'] - first_row['kafka_ts']) / 1000

max_diff = 0

query = data.aggregate([{'$group': {'_id': 1, "diff": {'$max': {'$abs': {'$subtract' : ['$consumer_ts', "$kafka_ts"]}} } } } ])

for r in query:
    max_diff = r['diff'] / 1000
    if max_diff is not None:
        break


print("{0:.2f} Mb/s".format((data_size / timing / (1024*1024))*8))
print(f"Max send/accept diff {str(max_diff)} seconds")



#filepath = 'D:/Sources/UCU/Kafka/02-kafka/data/timestamps.csv'
#
#columns = ['consumer_ts', 'kafka_ts', 'msg_size']
#
#df = pd.read_csv(filepath, names=columns, header=None)
#
#timing = (df.iloc[-1]['consumer_ts'] - df.iloc[0]['kafka_ts'])/1000
#
#data_size = (df['msg_size'].sum())
#
#max_dif = max(df['consumer_ts'] - df['kafka_ts'])/1000
#
#print("{0:.2f} Mb/s".format((data_size / timing / (1024*1024))*8))
#print(f"Max send/accept diff {str(max_dif)} seconds")