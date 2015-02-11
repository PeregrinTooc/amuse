from amuse.factory import JokeProviderFactory


class AbstractJokeProviderFactoryBuilder(object):
    """Builds a JokeProviderFactory.

    Note that you should not build a JokeProviderFactory directly; obtain
    one from an AbstractJokeProviderFactoryBuilder, which you obtain from
    AbstractJokeProviderFactoryBuilder.default().
    """

    def __init__(self):
        self._overrides = {}

    @classmethod
    def default(cls):
        return cls()

    def with_override(self, key, provider_cls):
        self._overrides[key] = provider_cls
        return self

    def build(self):
        factory = JokeProviderFactory()
        for key, cls_ in self._overrides.items():
            factory.register(key, cls_)
        return factory
