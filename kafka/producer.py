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
    data = json.loads(response.text)

    return data

def send_events():
    while(True):
        data = _produce_event()
        for row in data['data']:
            print('producing')
            producer.send(TOPIC_NAME, value=row)
        time.sleep(10) 


if __name__ == '__main__':
    send_events()