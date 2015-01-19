from amuse.providers.static import StaticJokeProvider


def amuse():
    return StaticJokeProvider("jokes.json").provide(context=None)
