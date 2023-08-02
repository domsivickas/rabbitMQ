import argparse
import pika

def create_exchange_and_queue(channel):
    exchange_name = 'test_exchange'
    queue_name = 'test_queue'
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
    channel.queue_declare(queue=queue_name, arguments={'x-message-ttl': 3600000})
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='')
    return exchange_name

def publish_sample_messages(channel, exchange_name):
    messages = ["Message 1", "Message 2", "Message 3"]
    for message in messages:
        channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
        print(f"Published: {message}")

def main():
    parser = argparse.ArgumentParser(description='RabbitMQ Producer Script')
    parser.add_argument('--username', required=True, help='RabbitMQ username')
    parser.add_argument('--password', required=True, help='RabbitMQ password')
    parser.add_argument('--vhost', required=True, help='RabbitMQ virtual host')
    args = parser.parse_args()

    credentials = pika.PlainCredentials(args.username, args.password)
    parameters = pika.ConnectionParameters('localhost', virtual_host=args.vhost, credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    try:
        exchange_name = create_exchange_and_queue(channel)
        publish_sample_messages(channel, exchange_name)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
