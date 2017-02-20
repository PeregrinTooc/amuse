"""Owns the joke. Publishes joke.told to the bus."""
import pika

from amuse.api import amuse


def serve():
    conn = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    ch = conn.channel()
    ch.queue_declare(queue="joke.told")
    ch.basic_publish(exchange="", routing_key="joke.told", body=amuse())
