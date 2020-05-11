"""Slash command handler: /amuse"""
from amuse.api import amuse


def handle(payload):
    return {
        "response_type": "in_channel",
        "text": amuse(),
    }
