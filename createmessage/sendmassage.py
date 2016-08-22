#!/usr/bin/env python
import pika
from pika.adapters import BlockingConnection
from pika import BasicProperties
connection = pika.BlockingConnection(pika.ConnectionParameters('172.20.14.192'))
#connection = BlockingConnection()

channel = connection.channel()

exchange_name = 'public'
routing_key = 'test_routing_key1'
while True:
	channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body='testing mirroring!', properties=BasicProperties(content_type="text/plain", delivery_mode=1))
	channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body='testing afternoon!', properties=BasicProperties(content_type="text/plain", delivery_mode=1))
	print "publish complete"

connection.close()
