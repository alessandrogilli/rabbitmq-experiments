import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('guest', 'guest')))

channel = connection.channel()

channel.exchange_declare(exchange='test-exchange', exchange_type='topic')

# Declare a durable queue
channel.queue_declare(queue='test-queue', durable=True)

# Bind the queue to the exchange
channel.queue_bind(exchange='test-exchange', queue='test-queue', routing_key='test-topic')

def callback(ch, method, properties, body):
    print(f"Received value: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test-queue', on_message_callback=callback, auto_ack=False)

channel.start_consuming()