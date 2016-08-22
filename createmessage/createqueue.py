#!/usr/bin/env python
import pika
from pika.adapters import BlockingConnection
from pika import BasicProperties

#connection = BlockingConnection('172.20.14.192')
connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.14.192'))
channel = connection.channel()

client_params = {"x-ha-policy": "all"}

exchange_name = 'public'
queue_name = 'test_queue1'
routing_key = 'test_routing_key1'

channel.exchange_declare(exchange=exchange_name, type='topic')

channel.queue_declare(queue=queue_name, durable=True, arguments=client_params )

channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

connection.close()
