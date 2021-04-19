import csv
import pandas as pd

filepath = 'D:/Sources/UCU/Kafka/02-kafka/data/timestamps.csv'

columns = ['consumer_ts', 'kafka_ts', 'msg_size']

df = pd.read_csv(filepath, names=columns, header=None)

timing = (df.iloc[-1]['consumer_ts'] - df.iloc[0]['kafka_ts'])/1000

data_size = (df['msg_size'].sum())

max_dif = max(df['consumer_ts'] - df['kafka_ts'])/1000

print("{0:.2f} MB/s".format(data_size / timing / (1024*1024)))
print(f"Max send/accept diff {str(max_dif)} seconds")