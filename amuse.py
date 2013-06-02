import random

JOKES = [
    "Why did the chicken cross the road? To get to the other side.",
    "I would tell you a UDP joke, but you might not get it.",
]


def amuse():
    return random.choice(JOKES)


if __name__ == "__main__":
    print(amuse())
