import time
import pika
import random



connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

channel.exchange_declare(exchange='test-exchange', exchange_type='topic')

while True:
    value = random.randint(1, 100)
    channel.basic_publish(exchange='test-exchange', routing_key='test-topic', body=str(value))
    print(f"Published value: {value}")
    time.sleep(1)

connection.close()
