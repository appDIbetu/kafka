import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS= "168.119.119.105:9094"
KAFKA_TOPIC="myTopic"
KAFKA_CONSUMER_GROUP="group-id"
loop = asyncio.get_event_loop()
