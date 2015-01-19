import json
import random

from amuse.providers.base import JokeProvider


class StaticJokeProvider(JokeProvider):
    def __init__(self, path):
        self._path = path

    def provide(self, context):
        with open(self._path) as fh:
            jokes = json.load(fh)["jokes"]
        return random.choice(jokes)["text"]

    @property
    def priority(self):
        return 100
