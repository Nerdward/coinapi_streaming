import requests
import time
import json

from kafka import KafkaProducer

TOPIC_NAME = 'assets'
URL = "http://api.coincap.io/v2/assets?"

PAYLOAD= {}
HEADERS = {}

producer = KafkaProducer(
    value_serializer= lambda msg: json.dumps(msg)\
        .encode('utf-8'),
    bootstrap_servers= ['localhost:9092']
)

def _produce_event():
    """
    Function to produce events
    """

    response = requests.request("GET", url=URL,headers=HEADERS, data=PAYLOAD)

    return response.text

def send_events():
    while(True):
        data = _produce_event()
        time.sleep(10) 
        print('producing')
        producer.send(TOPIC_NAME, value=data)


if __name__ == '__main__':
    send_events()