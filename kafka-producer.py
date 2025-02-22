import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=["3.87.73.168:9092"], 
                         value_serializer=lambda x: dumps(x).encode("utf-8"))

producer.send("demo_testing1", value = {"test": "test"})

stock_market_data = pd.read_csv("indexProcessed.csv")

print(stock_market_data.head())

while True:
    # print(stock_market_data.sample(1).to_dict(orient="records")[0])
    each_row = stock_market_data.sample(1).to_dict(orient="records")[0]
    producer.send("demo_testing1", value = each_row)

producer.flush()