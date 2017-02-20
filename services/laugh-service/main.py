"""Consumes joke.told. Laughs."""
import pika


def on_joke(ch, method, properties, body):
    print("ha")


def serve():
    conn = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    ch = conn.channel()
    ch.queue_declare(queue="joke.told")
    ch.basic_consume(on_joke, queue="joke.told", no_ack=True)
    ch.start_consuming()
