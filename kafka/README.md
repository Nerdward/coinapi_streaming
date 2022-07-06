## Instructions
1. ```
    pip install pipenv   
   ```


Pipenv is a virtual environment manager

2.
```
pipenv install kafka-python requests
```
kafka-python is Python's Kafka library

requests will be used to make API requests.

3. Start up kafka broker and zookeeper services
```bash
docker-compose up -d
```
> -d starts the containers in detached mode.


