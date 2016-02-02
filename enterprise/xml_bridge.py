"""Bridges the XML enterprise interface to the joke providers.

Per the integration specification agreed 2015-11-04, all inbound joke
requests arrive as JokeRequest documents conforming to JokeRequest.xsd.
"""
from amuse.builder import AbstractJokeProviderFactoryBuilder
from enterprise import utils, utils2  # noqa: F401


def handle(xml_bytes):
    factory = AbstractJokeProviderFactoryBuilder.default().build()
    provider = factory.create("static", path="jokes.json")
    joke = provider.provide(context=None)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<JokeResponse xmlns="urn:amuse:enterprise:joke:v1">'
        "<ResponseHeader><Status>OK</Status></ResponseHeader>"
        "<JokePayload><JokeText>" + joke + "</JokeText></JokePayload>"
        "</JokeResponse>"
    )
