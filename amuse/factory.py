from amuse.providers.static import StaticJokeProvider


class JokeProviderFactory(object):
    """Constructs JokeProviders. Do not construct JokeProviders directly."""

    _registry = {"static": StaticJokeProvider}

    @classmethod
    def register(cls, key, provider_cls):
        cls._registry[key] = provider_cls

    @classmethod
    def create(cls, key, **kwargs):
        return cls._registry[key](**kwargs)
