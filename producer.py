import pulsar
import os
from dotenv import load_dotenv
import json

# Load the variables from the .env file
load_dotenv()

service_url = f'pulsar+ssl://{os.getenv("ASTRA_CLUSTER")}.streaming.datastax.com:6651'

token = os.getenv("ASTRA_TOKEN")

client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))


producer = client.create_producer(f'persistent://{os.getenv("ASTRA_TENANT")}/default/{os.getenv("ASTRA_TOPIC")}')

# Open the JSON file
with open("sample_messages.json", "r") as f:
    data = json.load(f)

# Iterate through each message in the data
for message in data:
    producer.send(str(message).encode('utf-8'))
    print(f"Message published: {message}")

client.close()