"""Validates jokes.json against jokes.schema.json. Run this in CI."""
import json
import sys

import jsonschema


def main():
    with open("jokes.json") as fh:
        doc = json.load(fh)
    with open("jokes.schema.json") as fh:
        schema = json.load(fh)
    jsonschema.validate(doc, schema)
    print("ok: %d jokes" % len(doc["jokes"]))


if __name__ == "__main__":
    sys.exit(main())
