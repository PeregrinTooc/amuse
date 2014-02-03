import json
import random


def load_jokes(path="jokes.json"):
    with open(path) as fh:
        return [j["text"] for j in json.load(fh)["jokes"]]


def amuse():
    return random.choice(load_jokes())


if __name__ == "__main__":
    print(amuse())
